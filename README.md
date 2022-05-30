# Empresas

Aplicação que recebe dados referentes à empresas em arquivo formato `txt`, realiza
ETL sobre esse arquivo e disponibiliza as informações via api.


### Índice

- [Requirements](#requirements)
- [Setup](#setup)
- [API](API.md)
- [Testes](#testes)


### Requirements

- Python 3.7.*
- docker-compose 1.29.*


### Setup

Inicie os containers da stack
```bash
$ docker-compose up -d
```

Crie o ambiente virtual
```bash
$ python3.7 -m venv env
```

Ative o ambiente virtual
```bash
$ source env/bin/activate
```

Instale as dependências do projeto:
```bash
$ (env) pip install -r requirements/base.txt
```

Execute as migrations do projeto:
```bash
$ (env) python3 manage.py migrate
```

Acesse a aplicação localmente usando a seguinte url: `http://127.0.0.1:8000`


### Testes

Execute os testes:
```bash
$ (env) pytest
```
