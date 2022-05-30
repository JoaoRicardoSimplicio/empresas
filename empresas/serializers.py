from rest_framework import serializers

from empresas.models import Empresa, Relatorio


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'comprador',
            'descricao',
            'preco',
            'quantidade',
            'endereco',
        )
        model = Empresa


class RelatorioSerializer(serializers.ModelSerializer):

    empresas = EmpresaSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'nome',
            'total',
            'empresas',
        )
        model = Relatorio
