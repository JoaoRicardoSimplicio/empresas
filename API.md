# Salva empresas / Gera relatório

Acesse o browser na seguinte url e faça upload do arquivo
com dados das empresas.

**URL**: `/`

**Método**: `POST`

**Autenticação requerida**: `NO`


# Lista empresas

Use essa url para listar empresas

**URL**: `/empresas/`

**Método**: `GET`

**Autenticação requerida**: `NO`

**Modelo Requisição**

```bash
    curl -X GET http://127.0.0.1:8000/empresas/
```


# Obtem empresa

Use essa url para obter empresa

**URL**: `/empresas/<int:pk>/`

**Método**: `GET`

**Autenticação requerida**: `NO`

**Modelo Requisição**

```bash
    curl -X GET http://127.0.0.1:8000/empresas/1/
```


# Lista relatórios

Use essa url para listar relatórios

**URL**: `/relatorios/`

**Método**: `GET`

**Autenticação requerida**: `NO`

**Modelo Requisição**

```bash
    curl -X GET http://127.0.0.1:8000/relatorios/
```


# Obtem relatório

Use essa url para obter relatório

**URL**: `/relatorios/<str:nome>/`

**Método**: `GET`

**Autenticação requerida**: `NO`

**Modelo Requisição**

```bash
    curl -X GET http://127.0.0.1:8000/relatorios/relatorio_nome/
```
