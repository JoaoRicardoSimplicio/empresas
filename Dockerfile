FROM python:3.7

ENV PYTHONPATH /app

WORKDIR /app
COPY ./requirements/base.txt /app
RUN pip install --upgrade pip
RUN pip install -r base.txt
COPY . /app
