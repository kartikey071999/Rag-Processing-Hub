from typing import Any
from fastapi import APIRouter
from app import constants

router = APIRouter()


@router.get("/api/version")
async def get_version() -> Any:
    """
    Get Application Version.
    """
    VERSION = constants.APP_VERSION
    return {"version": VERSION}
