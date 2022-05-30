from io import TextIOWrapper

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from rest_framework import (
    filters,
    generics,
    views
)

from empresas.models import (
    Empresa,
    Relatorio
)
from empresas.paginacao import RelatorioPaginacao
from empresas.serializers import (
    EmpresaSerializer,
    RelatorioSerializer
)
from empresas.tarefas.salva import salva_relatorio


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')

    def post(self, request, format=None):
        arquivo = TextIOWrapper(request.FILES['empresas'].file, encoding='utf-8')
        nome_arquivo = request.FILES['empresas'].name
        relatorio = salva_relatorio(arquivo, nome_arquivo)
        url = f'/relatorios/{relatorio}/' if relatorio else '/relatorios/'
        return HttpResponseRedirect(redirect_to=url)


class RelatorioListView(generics.ListAPIView):

    description = 'Lista relatórios'
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    pagination_class = RelatorioPaginacao
    filter_backends = [filters.OrderingFilter]
    ordering = ['-id']


class RelatorioDetailView(generics.RetrieveAPIView):

    description = 'Obtem relatório'
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    lookup_field = 'nome'


class EmpresaListView(generics.ListAPIView):

    description = 'Lista empresas'
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['-id']


class EmpresaDetailView(generics.RetrieveAPIView):

    description = 'Obtem empresa'
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    lookup_fields = ['id']
