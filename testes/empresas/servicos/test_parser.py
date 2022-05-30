from pathlib import Path
from unittest import TestCase

from empresas.servicos.parser import Parser


BASE_DIR = Path(__file__).parent


RESULTADOS = [
    {"comprador": "João Silva", "descricao": "R$10 off R$20 of food", "preco": 10.0, "quantidade": 2, "endereco": "987 Fake St Bob's Pizza"},
    {"comprador": "João", "descricao": "Promoção A", "preco": 5.10, "quantidade": 45, "endereco": "Rua desconhecida, 23"},
    {"comprador": "Pedro Rafael Souza", "descricao": "Cupom B", "preco": 23.3, "quantidade": 4, "endereco": "Av. Joaquim, 117"},
    {"comprador": "A", "descricao": "Cupom C", "preco": 20.0, "quantidade": 12, "endereco": "Rua A, 11"},
    {"comprador": "Amy Pond", "descricao": "R$30 of awesome for R$10", "preco": 10.0, "quantidade": 5, "endereco": "456 Unreal Rd Tom's Awesome Shop"},
    {"comprador": "Snake Plissken", "descricao": "R$20 Sneakers for R$5", "preco": 5.0, "quantidade": 4, "endereco": "123 Fake St Sneaker Store Emporium"},
    {"comprador": "Marty McFly", "descricao": "R$20 Sneakers for R$5", "preco": 5.0, "quantidade": 1, "endereco": "123 Fake St Sneaker Store Emporium"},
    {"comprador": "João Ricardo Ricardo Richard", "descricao": "R$10 off R$20 of food", "preco": 123.23, "quantidade": 1000, "endereco": "456 Unreal Rd Tom's Awesome Shop"},
    {"comprador": "joão icardo ricardo Richard", "descricao": "R$10 off R$20 of food", "preco": 123.23, "quantidade": 1000, "endereco": '456 unreal Rd Tom"s Awesome Shop'},
    {"comprador": "ricardo ricardo Richard", "descricao": "R$10 off R$20 of food", "preco": 123.23, "quantidade": 2000, "endereco": '456 unreal Rd Tom"s Awesome Shop'},
    {"comprador": "Paul Pond", "descricao": "R$30 of awesome for R$10", "preco": 10.0, "quantidade": 15, "endereco": "456 Unreal Rd Tom's Awesome Shop"},
]

class TestParser(TestCase):

    def setUp(self):
        self.parser_dados_empresas = Parser(open(f'{BASE_DIR}/fixtures/dados.txt'))
        self.parser_formato_incompativel = Parser(open(f'{BASE_DIR}/fixtures/dados_incorretos.txt'))

    def test_obtem_dados_empresas_corretamente(self):
        empresas = self.parser_dados_empresas.executar()
        for resultado in RESULTADOS:
            self.assertIn(resultado, empresas)

    def test_falha_obter_dados_arquivo_formato_incompativel_parser(self):
        empresas = self.parser_formato_incompativel.executar()
        self.assertEqual([], empresas)
