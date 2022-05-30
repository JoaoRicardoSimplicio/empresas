import re

from typing import IO


class Parser:

    def __init__(self, arquivo: IO[str]) -> None:
        self.conteudo = arquivo.readlines()

    def executar(self) -> list:
        self._remove_cabecalhos()
        return self._obtem_dados_empresas()

    def _remove_cabecalhos(self) -> None:
        self.conteudo.pop(0)

    def _obtem_dados_empresas(self) -> list:
        regex_dados = (
            r'(?:'
            r'(?P<comprador>^(?:[\w\s])+)(?:\s{2,}|\t|\\t)'
            r'(?P<descricao>(?:[\$\w\d]+ *[\$\w\d])+)(?:\s{2,}|\t|\\t)'
            r'(?P<preco>[\d\.\,]+)(?:\s{2,}|\t|\\t)'
            r'(?P<quantidade>\d{1,5})(?:\s{2,}|\t|\\t)'
            r'(?P<endereco>(?:(?:[\d\w\s\'\"\,\.]|\\t)+)+)'
            r')'
        )
        regex_sub = '(?:\t)+'
        regex_dados_compilada = re.compile(regex_dados)
        regex_sub_compilada = re.compile(regex_sub)
        empresas = []
        for linha in self.conteudo:
            empresa = self._obtem_dados_empresa(linha, regex_dados_compilada, regex_sub)
            if empresa:
                empresas.append(empresa)
        return empresas
            
    def _obtem_dados_empresa(self, linha, regex_dados, regex_substituicao) -> dict:
        match = regex_dados.match(linha)
        try:
            empresa = {
                'comprador': re.sub(regex_substituicao, ' ', match.group('comprador')).strip(),
                'descricao': re.sub(regex_substituicao, ' ', match.group('descricao')).strip(),
                'preco': float(match.group('preco')),
                'quantidade': int(match.group('quantidade')),
                'endereco': re.sub(regex_substituicao, ' ', match.group('endereco')).strip()
            }
        except AttributeError:
            empresa = None
        return empresa
