from django.urls import path

from empresas.views import (
    EmpresaDetailView,
    EmpresaListView,
    HomeView,
    RelatorioDetailView,
    RelatorioListView
)


app_name = 'empresas'


urlpatterns = [
    path('', HomeView.as_view()),
    path('empresas/', EmpresaListView.as_view()),
    path('empresas/<int:pk>/', EmpresaDetailView.as_view()),
    path('relatorios/', RelatorioListView.as_view()),
    path('relatorios/<str:nome>/', RelatorioDetailView.as_view()),
]
