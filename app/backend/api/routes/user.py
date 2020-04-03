from typing import Mapping, Sequence

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.backend.db.models import UserOps
from app.backend.schema import UserWithID

router = APIRouter()


@router.get("", response_model=Sequence[UserWithID], name="users:get-current-user")
async def retrieve_all_user(ops: UserOps = Depends(),) -> Sequence[Mapping]:
    items = await ops.select_all()
    return items
