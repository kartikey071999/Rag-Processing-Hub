import uuid
import uuid
from fastapi import APIRouter
from app.database.sqlalchemy import FileStatusRepository
from app.database.schemas import Files

router = APIRouter()

@router.get("/file/{file_id}")
async def request_file_record(file_id: uuid.UUID)->Files:
    file_record: Files = FileStatusRepository.get_by_file_by_file_id(file_id = file_id)
    return file_record



