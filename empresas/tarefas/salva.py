from typing import IO

from empresas.models import Empresa, Relatorio
from empresas.servicos.parser import Parser


def salva_empresa(empresa: dict) -> Empresa:
    try:
        return Empresa.objects.create(**empresa)
    except Exception:
        pass


def salva_relatorio(arquivo: IO[str], nome_arquivo: str = None) -> str:
    parser = Parser(arquivo=arquivo)
    nome_arquivo = arquivo.name.split('/')[-1].split('.')[0] \
        if not nome_arquivo \
        else nome_arquivo.split('.')[0]
    empresas = parser.executar()
    if len(empresas) < 1 or Relatorio.objects.filter(nome=nome_arquivo).exists():
        return
    relatorio = Relatorio.objects.create(nome=nome_arquivo)
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
