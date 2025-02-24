import uuid
import uuid
from fastapi import APIRouter
from database.sql_alchemy import FileStatusRepository

router = APIRouter()

def request_file_record(file_id: uuid.UUID):


