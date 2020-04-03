from pydantic import BaseModel


class IDMixin(BaseModel):
    id: int = 0
