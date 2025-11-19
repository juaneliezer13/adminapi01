import os

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://admin:admin123@admin-database:5432/adminapidb"
)
SECRET_KEY = os.getenv("SECRET_KEY", "admin123")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

