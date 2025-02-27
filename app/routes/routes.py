from fastapi import APIRouter
from app.routes import file_crud

all_api_routes = APIRouter()

all_api_routes.include_router(file_crud.router, tags=["File CRUD"])



