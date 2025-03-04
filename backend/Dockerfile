FROM python:3.12.2

RUN mkdir /backend

WORKDIR /backend

COPY poetry.lock* pyproject.toml ./

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false # чтобы ставилось в корень
RUN poetry install --no-root

COPY ./. /backend/.
