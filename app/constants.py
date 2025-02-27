import os
import json

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
APP_VERSION = "local-dev"

# sql Credentials
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
ASYNC_DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"


# Print values to verify (optional, remove in production)
if __name__ == "__main__":
    print("DB_USER:", DB_USER)
    print("DB_HOST:", DB_HOST)
    print("ASYNC_DB_URL:", ASYNC_DB_URL)