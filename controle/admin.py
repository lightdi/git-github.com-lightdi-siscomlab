from django.contrib import admin
from .models import Laboratorio, Maquina,Problema

# Register your models here.
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'linhas', 'colunas')
    search_fields = ('nome',)

@admin.register(Maquina)
class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'laboratorio', 'linha', 'coluna')
    search_fields = ('nome',)
    list_filter = ('laboratorio',)

@admin.register(Problema)
class ProblemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'maquina', 'descricao', 'resolvido')
    search_fields = ('maquina', 'descricao')
    list_filter = ('resolvido',)
