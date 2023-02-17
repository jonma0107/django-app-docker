FROM python:3.9.16-alpine3.17

ENV PYTHONUNBUFFERED 1

# RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt ./
RUN python -m pip install -r requirements.txt

COPY . .

# RUN adduser -D user
# USER user







