import logging

from app.routes import all_api_routes
from fastapi import FastAPI, HTTPException, Request, status
from contextlib import asynccontextmanager
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

logging.basicConfig(
    level=logging.DEBUG,  # Ensure INFO and DEBUG logs are captured
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()  # Log to console
    ]
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("application is duuiug")
    yield
app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"tryItOutEnabled": True})
app.include_router(all_api_routes)


@app.exception_handler(Exception)
async def catch_all_exception_handler(request, exc):
    logging.error(f"An unexpected exception has occurred! {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({"error_message": "opps something went wrong!"}),
    )
