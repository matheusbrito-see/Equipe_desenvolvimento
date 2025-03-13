from django.db import models
from django.utils import timezone

class Setores(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=100)
    setor_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)  # Adicionei unique=True para evitar emails duplicados
    senha_hash = models.CharField(max_length=255)
    perfil = models.CharField(max_length=100, default="padrao")  
    setor = models.ForeignKey(Setores, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    ultimo_login = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome
    
    def __str__(self):
        return self.nome
    
    def __str__(self):
        return self.nome
    
class Tipo_material(models.Model):
    nome_tipo = models.CharField(max_length=255)
    status = models.BooleanField(default=True, verbose_name="Status")
    
    def __str__(self):
        return self.nome_tipo
    
class Area_utilizacao(models.Model):
    nome_area = models.CharField(max_length=255)
    status = models.BooleanField(default=True, verbose_name="Status")
    
    def __str__(self):
        return self.nome_area
    
class Unidade_medida(models.Model):
    descricao_unidade = models.CharField(max_length=255)
    status = models.BooleanField(default=True, verbose_name="Status")
    
    def __str__(self):
        return self.descricao_unidade
    
class Itens(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField()
    tipo = models.ForeignKey(Tipo_material, on_delete=models.CASCADE)
    area = models.ForeignKey(Area_utilizacao, on_delete=models.CASCADE, null=True, blank=True)
    unidade_medida = models.ForeignKey(Unidade_medida, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.codigo} - {self.descricao}"
    
class Lista_planejamento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setores, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[("Aberto", "aberto"), ("Fechado", "fechado")])
    data_fechamento = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Planejamento {self.id} - {self.status}"
    
class Itens_lista(models.Model):
    lista_planejamento = models.ForeignKey(Lista_planejamento, on_delete=models.CASCADE, default=1)
    item = models.ForeignKey(Itens, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.item.descricao} - {self.quantidade}"
    