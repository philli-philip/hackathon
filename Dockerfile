FROM nikolaik/python-nodejs:python3.8-nodejs13

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.0.* && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . ./

CMD alembic upgrade head && \
    gunicorn --bind 0.0.0.0:$PORT -w 2 -k uvicorn.workers.UvicornWorker app.backend.main:app
