from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Laboratorio, Maquina, Problema
from .forms import ProblemaForm

# Create your views here.

@login_required
def index(request):

    laboratorio = Laboratorio.objects.all()

    return render(request, 'index.html', {'laboratorios': laboratorio})

@login_required
def laboratorio(request, id):
    laboratorio = get_list_or_404(Laboratorio, id=id)[0]
    maquinas = Maquina.objects.filter(laboratorio=laboratorio)


     # Criar uma matriz representando as linhas e colunas
    tabela = [[None for _ in range(laboratorio.colunas)] for _ in range(laboratorio.linhas)]


    # Preencher a matriz com as máquinas
    for maquina in maquinas:
        tabela[maquina.linha][maquina.coluna] = maquina

    return render(request, 'laboratorio.html', {
        'laboratorio': laboratorio,
        'maquinas': maquina,
        'tabela': tabela,
        })

@login_required
def informar_problema(request, id):
    maquina = get_list_or_404(Maquina, id=id)[0]
    print(maquina)
    print(request.method)
    if request.method == 'POST':
        form = ProblemaForm(request.POST)
        if form.is_valid():
            problema = form.save(commit=False)
            problema.maquina = maquina
            problema.save()
            messages.success(request, 'Problema informado com sucesso!')
            return redirect('index')
    else:
        form = ProblemaForm(initial={'maquina': maquina})
        print("form")

    return render(request, 'informar_problema.html', {'form': form, 'maquina': maquina})
