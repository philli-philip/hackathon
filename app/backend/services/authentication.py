from app.backend.db.errors import EntityDoesNotExist
from app.backend.db.models import UserOps


async def check_username_is_taken(ops: UserOps, username: str) -> bool:
    try:
        await ops.get_user_by_username(username=username)
    except EntityDoesNotExist:
        return False

    return True


async def check_email_is_taken(ops: UserOps, email: str) -> bool:
    try:
        await ops.get_user_by_email(email=email)
    except EntityDoesNotExist:
        return False

    return True
