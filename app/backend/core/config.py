import logging
import shlex
import subprocess
import sys
from typing import List

from databases import DatabaseURL
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from app.backend.core.logging import InterceptHandler

config = Config(".env")


class Config:
    API_PREFIX = "/api"

    JWT_TOKEN_PREFIX = "Token"  # noqa: S105
    VERSION = "0.0.0"

    DEBUG: bool = config("DEBUG", cast=bool, default=False)

    MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
    MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)

    SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)

    PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI example application")
    ALLOWED_HOSTS: List[str] = config("ALLOWED_HOSTS", cast=CommaSeparatedStrings, default="")

    # logging configuration
    LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
    logging.basicConfig(handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL)
    logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])


class DevelopmentConfig(Config):
    ENV: str = "development"
    DEBUG: bool = True
    cmd = shlex.split("heroku config:get HEROKU_POSTGRESQL_PINK_URL -a ubsvsvirus")
    p = subprocess.run(cmd, stdout=subprocess.PIPE)
    DATABASE_URL = p.stdout.decode().strip().replace("postgres","postgresql")


class ProductionConfig(Config):
    ENV: str = "production"
    cmd = shlex.split("heroku config:get DATABASE_URL -a ubsvsvirus")
    p = subprocess.run(cmd, stdout=subprocess.PIPE)
    DATABASE_URL = p.stdout.decode().strip().replace("postgres","postgresql") 


config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}


def get_config(config_name: str = None) -> Config:
    if config_name is None:
        config_name: str = config("APP_CONFIG", default="development")
    return config_dict[config_name]


app_config = get_config()
