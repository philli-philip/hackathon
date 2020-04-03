FROM python:3.8.2

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.0.* && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . ./

CMD alembic upgrade head && \
    gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.backend.main:app
