import uuid
import uuid
from fastapi import APIRouter, status
from app.database.sqlalchemy import FileStatusRepository
from app.database.schemas import Files
import logging
from fastapi.responses import JSONResponse
router = APIRouter()
logger = logging.getLogger("uvicorn")

@router.get("/file/{file_id}", status_code=status.HTTP_200_OK)
async def request_file_record(file_id: uuid.UUID)->Files:

    logger.info("hit file get api")
    file_record: Files = FileStatusRepository.get_by_file_by_file_id(file_id = file_id)
    return file_record



