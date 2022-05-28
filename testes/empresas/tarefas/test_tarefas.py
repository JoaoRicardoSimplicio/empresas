from django.test import TransactionTestCase
from unittest import mock

from empresas.models import Empresa, Relatorio
from empresas.tarefas.salva import (
    salva_empresa,
    salva_relatorio
)


class TestTarefas(TransactionTestCase):

    def setUp(self):
        pass

    def test_salva_empresa_dados_corretos(self):
        empresa = {
            "comprador": "João Silva",
            "descricao": "R$10 off",
            "preco": 10.0,
            "quantidade": 2,
            "endereco": "987 Fake"
        }
        salva_empresa(empresa)
        self.assertEqual(1, Empresa.objects.count())
        self.assertEqual(empresa['comprador'], Empresa.objects.first().comprador)

    def test_falha_salva_empresa_dados_inexistentes(self):
        empresa = {
            "comprador": "Silva",
            "descricao": "R$10 off",
            "endereco": "987 Fake"
        }
        salva_empresa(empresa)
        self.assertEqual(0, Empresa.objects.count())

    @mock.patch('empresas.tarefas.salva.Parser.executar')
    @mock.patch("builtins.open", create=True)
    def test_salva_relatorio_corretamente(self, mock_arquivo, mock_empresas):
        mock_arquivo.return_value.name = 'dados.txt'
        mock_empresas.return_value = [
            {"comprador": "João R.", "descricao": "R$10 off", "preco": 10.0, "quantidade": 2, "endereco": "987 Fake"},
            {"comprador": "João", "descricao": "R$10 off", "preco": 10.0, "quantidade": 2, "endereco": "987 Fake"}
        ]
        arquivo = open('dados.txt', 'r')
        relatorio = salva_relatorio(arquivo)
        self.assertEqual(2, Empresa.objects.count())
        self.assertTrue(Empresa.objects.filter(comprador='João R.').exists())
        self.assertTrue(Empresa.objects.filter(comprador='João').exists())
        self.assertEqual(1, Relatorio.objects.count())
        self.assertEqual(20.00, Relatorio.objects.first().total)

    @mock.patch('empresas.tarefas.salva.Parser.executar')
    @mock.patch("builtins.open", create=True)
    def test_salva_relatorio_somente_empresas_salvas(self, mock_arquivo, mock_empresas):
        mock_arquivo.return_value.name = 'dados.txt'
        mock_empresas.return_value = [
            {"comprador": "João R.", "descricao": "R$10 off", "preco": 10.0, "quantidade": 2, "endereco": "987 Fake"},
            {"comprador": "João", "descricao": "R$10 off", "preco": 12.0, "quantidade": 2, "endereco": "987 Fake"},
            {"comprador": "João Victor", "descricao": "R$10 off", "preco": 10.0, "quantidade": 2, "endereco": "987 Fake"},
            {"compr": "João", "descricao": "R$10 off", "prco": 12.0, "quantidade": 2, "endereco": "987 Fake"}
        ]
        arquivo = open('dados.txt', 'r')
        relatorio = salva_relatorio(arquivo)
        self.assertEqual(3, Empresa.objects.count())
        self.assertEqual(32.00, Relatorio.objects.first().total)
