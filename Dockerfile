FROM python:3.12-alpine

MAINTAINER Some Dev

# спосіб 1
#ENV PYTHONUNBUFFERED=1

# спосіб 2
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2 \
    POETRY_NO_INTERACTION=1 \
    DEBIAN_FRONTEND=noninteractive \
    COLUMNS=80

RUN apk update
RUN apk add --no-cache gcc musl-dev mariadb-dev
# спосіб 2
RUN apk add --no-cache curl

#for pillow
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg

RUN mkdir /app
WORKDIR /app

#спосіб 1
#RUN pip install --upgrade pip
#спосіб 1
#COPY requirements.txt /tmp
#спосіб 1
#RUN cd /tmp && pip install -r requirements.txt

#спосіб 2
ENV POETRY_HOME=/usr/local/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /usr/local/poetry/bin/poetry /usr/bin/poetry
ENV PATH=$POETRY_HOME/bin:$PATH
#спосіб 2
COPY pyproject.toml poetry.lock /app/
#спосіб 2
RUN poetry config virtualenvs.create false && poetry install --no-ansi
