FROM python:3.10.9-alpine3.17

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./
RUN python -m pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user







