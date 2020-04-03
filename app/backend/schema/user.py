from pydantic import BaseModel

from .base import IDMixin


class User(BaseModel):
    username: str
    email: str


class UserWithID(IDMixin, User):
    pass
