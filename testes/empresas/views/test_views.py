from django.test import TestCase

from model_bakery import baker
from pathlib import Path

from empresas.models import (
    Empresa,
    Relatorio
)


BASE_DIR = Path(__file__).parent


class TestViews(TestCase):

    def setUp(self):
        self.relatorio = baker.make(Relatorio, total=100, nome='teste')
        self.empresas = baker.make(Empresa, relatorio=self.relatorio, _quantity=5)

    def test_lista_relatorios_corretamente(self):
        baker.make(Relatorio, total=150, nome='teste2')
        resposta = self.client.get('/relatorios/')
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()['count'], 2)

    def test_obtem_relatorio_corretamente(self):
        resposta = self.client.get('/relatorios/teste/')
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()['nome'], 'teste')
        self.assertEqual(len(resposta.json()['empresas']), 5)

    def test_falha_obter_relatorio_inexistente(self):
        resposta = self.client.get('/relatorios/inexistente/')
        self.assertEqual(resposta.status_code, 404)
        self.assertEqual(resposta.json(), {'detail': 'Not found.'})

    def test_lista_empresas_corretamente(self):
        resposta = self.client.get('/empresas/')
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()['count'], 5)

    def test_obtem_empresa_corretamente(self):
        resposta = self.client.get(f'/empresas/{self.empresas[0].id}/')
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()['id'], self.empresas[0].id)

    def test_falha_obter_empresa_inexistente(self):
        resposta = self.client.get('/empresas/30/')
        self.assertEqual(resposta.status_code, 404)
        self.assertEqual(resposta.json(), {'detail': 'Not found.'})

    def test_obtem_home_view(self):
        resposta = self.client.get('/')
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'home.html')

    def test_salva_empresas_e_relatorio_corretamente(self):
        with open(f'{BASE_DIR}/fixtures/dados.txt', 'rb') as fp:
            resposta = self.client.post('/', {'name': 'empresas', 'empresas': fp})
            relatorio = Relatorio.objects.get(nome='dados')
            self.assertEqual(resposta.status_code, 302)
            self.assertEqual(resposta.url, '/relatorios/dados/')
            self.assertEqual(relatorio.total, 30.00)
            self.assertEqual(relatorio.empresas.count(), 4)

    def test_falha_salva_empresas_e_relatorio_corretamente(self):
        with open(f'{BASE_DIR}/fixtures/dados_incorretos.txt', 'rb') as fp:
            resposta = self.client.post('/', {'name': 'empresas', 'empresas': fp})
            self.assertEqual(resposta.status_code, 302)
            self.assertEqual(resposta.url, '/relatorios/')
            self.assertFalse(Relatorio.objects.filter(nome='dados_incorretos').exists())
