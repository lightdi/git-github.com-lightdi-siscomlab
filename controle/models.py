from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    linhas = models.IntegerField()
    colunas = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Maquina(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    linha = models.IntegerField(default=0)
    coluna = models.IntegerField(default=0)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Problema(models.Model):
    id = models.AutoField(primary_key=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=500)
    resolvido = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao


