from django.db import models
from django.utils import timezone

class Setor(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=100)
    setor_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome
    
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    senha_hash = models.CharField(max_length=255)
    perfil = models.CharField(max_length=100)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    ultimo_login = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nome
    
class TipoMaterial(models.Model):
    nome_tipo = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nome_tipo
    
class AreaUtilizacao(models.Model):
    nome_area = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nome_area
    
class UnidadeMedia(models.Model):
    descricao_unidade = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.descricao__unidade
    
class Item(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField()
    tipo = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE)
    AreaUtilizacao = models.ForeignKey(AreaUtilizacao, on_delete=models.CASCADE)
    unidade-medida = models.ForeignKey(UnidadeMedia, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"s{self.codigo} - {self.descricao}"
    
class Listaplanejamento(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[("Aberto", "aberto"), ("Fechado", "fechado")])
    data_fechamento = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Planejamento {self.id} - {self.status}"
    
class ItensLista(models.Model):
    lista = models.ForeignKey(Listaplanejamento, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"`{self.item} - {self.quantidade}"
    