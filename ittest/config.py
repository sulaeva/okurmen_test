import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")  # Загружает переменные из .env


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-fallback-key-change-in-production")
    DEBUG = os.getenv("DEBUG", "False") == "True"
    ALLOWED_HOSTS = [host.strip() for host in os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",") if host.strip()]

    DATABASES = {
        "default": dj_database_url.config(
            default=os.getenv("DATABASE_URL", "sqlite:///db.sqlite3"),
            conn_max_age=600,
        )
    }

    STATIC_URL = "/static/"
    STATIC_ROOT = BASE_DIR / "staticfiles"

    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"