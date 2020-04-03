from databases import Database

from app.backend.core.config import app_config

database = Database(
    app_config.DATABASE_URL,
    min_size=app_config.MIN_CONNECTIONS_COUNT,
    max_size=app_config.MAX_CONNECTIONS_COUNT,
    ssl="require",
)
