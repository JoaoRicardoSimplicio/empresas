from rest_framework.pagination import PageNumberPagination


class RelatorioPaginacao(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'itens_pagina'
    max_page_size = 50
