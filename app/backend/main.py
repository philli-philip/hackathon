from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from app.backend.api.errors.http_error import http_error_handler
from app.backend.api.errors.validation_error import http422_error_handler
from app.backend.api.routes import router as api_router
from app.backend.core.config import app_config
from app.backend.db import database


def get_application() -> FastAPI:
    application = FastAPI(
        title=app_config.PROJECT_NAME, debug=app_config.DEBUG, version=app_config.VERSION
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=app_config.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @application.on_event("startup")
    async def start_app():
        await database.connect()

    @application.on_event("shutdown")
    async def stop_app():
        await database.disconnect()

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=app_config.API_PREFIX)
    application.mount("/static", StaticFiles(directory="app/static"), name="static")
    application.mount("/assets", StaticFiles(directory="app/static/assets"), name="static")

    @application.get("/", response_class=HTMLResponse)
    async def read_root():
        with open("app/static/index.html", "r") as f:
            return f.read()

    return application


app = get_application()
