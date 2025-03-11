from django.db import models
from django.utils import timezone

class setor(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=100)
    setor_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome
    
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    senha = models.CharField(max_length=255)
    setor = models.ForeignKey(setor, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome
    
class TipoMaterial(models.Model):
    nome_tipo = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nome_tipo
    
class AreaAutorizacao(models.Model):
    nome_area = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nome_area
    
class UnidadeMedia(models.Model):
    nome_unidade = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.descricao_unidade
    
class item(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField()
    tipo = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"s{self.codigo} - {self.descricao}"
    
class Listaplanejamento(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    setor = models.ForeignKey(setor, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[("Aberto", "aberto"), ("Fechado", "fechado")])
    data_fechamento = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.Usuario} - {self.descricao}"()