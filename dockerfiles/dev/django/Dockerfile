FROM python:3.12-alpine

LABEL maintainer="ali.ahadi.official@gmail.com"

WORKDIR /usr/src/app

COPY ./requirements.txt .

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user


USER django-user   




COPY ./core .

