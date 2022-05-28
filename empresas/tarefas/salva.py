from typing import IO

from empresas.models import Empresa
from empresas.servicos.parser import Parser


def salva_empresa(empresa: dict) -> None:
    try:
        Empresa.objects.create(**empresa)
    except Exception:
        pass


def salva_empresas(arquivo: IO[str]) -> None:
    parser = Parser(arquivo=arquivo)
    empresas = parser.executar()
    for empresa in empresas:
        salva_empresa(empresa=empresa)
