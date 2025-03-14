from django.shortcuts import render

from .models import Setor, Usuario, TipoMaterial, AreaUtilizacao, UnidadeMedia, Item, Listaplanejamento, ItensLista, itemPlanejado
from .serializers import(
    ItemPlanejadoSerializer,
    SetorSerializer,
    UsuarioSerializer,
    TipoMaterialSerializer,
    AreaUtilizacaoSerializer,
    UnidadeMediaSerializer,
    ItemSerializer,
    ListaplanejamentoSerializer,
    ItensListaSerializer
)
from rest_framework import viewsets

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all() 
    serializer_class = SetorSerializer
    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class TipoMaterialViewSet(viewsets.ModelViewSet):
    queryset = TipoMaterial.objects.all()
    serializer_class = TipoMaterialSerializer
    
class AreaUtilizacaoViewSet(viewsets.ModelViewSet):
    queryset = AreaUtilizacao.objects.all()
    serializer_class = AreaUtilizacaoSerializer
    
class UnidadeMediaViewSet(viewsets.ModelViewSet):
    queryset = UnidadeMedia.objects.all()
    serializer_class = UnidadeMediaSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ListaplanejamentoViewSet(viewsets.ModelViewSet):
    queryset = Listaplanejamento.objects.all()
    serializer_class = ListaplanejamentoSerializer
    
class ItensListaViewSet(viewsets.ModelViewSet):
    queryset = ItensLista.objects.all()
    serializer_class = ItensListaSerializer

class ItemPlanejadoViewSet(viewsets.ModelViewSet):
    queryset = itemPlanejado.objects.all()
    serializer_class = ItemPlanejadoSerializer

class ItensListaViewSet(viewsets.ModelViewSet):
    queryset = ItensLista.objects.all()
    serializer_class = ItensListaSerializer
    
