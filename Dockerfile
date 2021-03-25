FROM python:3.8

ENV APP_PATH=/code \
    POETRY_VIRTUALENVS_IN_PROJECT=true

RUN pip install poetry

WORKDIR $APP_PATH

COPY . .
RUN poetry install
