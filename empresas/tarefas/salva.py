from typing import IO

from empresas.models import Empresa, Relatorio
from empresas.servicos.parser import Parser


def salva_empresa(empresa: dict) -> Empresa:
    try:
        return Empresa.objects.create(**empresa)
    except Exception:
        pass


def salva_relatorio(arquivo: IO[str]) -> str:
    parser = Parser(arquivo=arquivo)
    nome_arquivo = arquivo.name.split('/')[-1]
    relatorio = Relatorio.objects.create(nome=nome_arquivo)
    empresas = parser.executar()
    total = 0
    for empresa in empresas:
        empresa_salva = salva_empresa(empresa=empresa)
        if empresa_salva:
            total += empresa_salva.preco
            empresa_salva.relatorio = relatorio
            empresa_salva.save()
    relatorio.total = total
    relatorio.save()
    return relatorio.nome
