FROM python:3.10-slim-buster

LABEL maintainer="ali.ahadi.official@gmail.com"

WORKDIR /usr/src/app

COPY ./requirements.txt .

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./core .