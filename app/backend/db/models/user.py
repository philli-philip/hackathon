from sqlalchemy import Column, Integer, Table, Text

from .. import database
from . import metadata

user = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", Text, nullable=False),
    Column("email", Text, nullable=False),
)


class UserOps:
    async def select_all(self):
        query = user.select()
        items = await database.fetch_all(query)
        return items
