from fastapi import APIRouter
from app.routes import file_crud, version

all_api_routes = APIRouter()


all_api_routes.include_router(version.router, tags=["Version"])
all_api_routes.include_router(file_crud.router, tags=["File CRUD"])



