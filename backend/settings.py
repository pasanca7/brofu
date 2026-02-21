import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="settings.env")

THESPORTSDB_API_URL = os.getenv("THESPORTSDB_API_URL")

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_URL = os.getenv("DATABASE_URL")

ORIGINS = os.getenv("FRONTEND_ORIGINS", "").split(",")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
