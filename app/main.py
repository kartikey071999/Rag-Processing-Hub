from app.routes import all_api_routes
from fastapi import FastAPI, HTTPException, Request, status



app = FastAPI( swagger_ui_parameters={"tryItOutEnabled": True})
app.include_router(all_api_routes)