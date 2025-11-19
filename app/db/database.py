import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import DATABASE_URL


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def wait_for_db(retries: int = 10, delay_seconds: int = 2) -> None:
    """
    Intenta conectar a la base de datos varias veces antes de rendirse.
    """
    attempts = retries
    while attempts > 0:
        try:
            with engine.connect():
                print("✅ Conexión a Base de Datos exitosa.")
                return
        except OperationalError:
            attempts -= 1
            print(
                f"⏳ Base de datos no lista, reintentando en {delay_seconds} segundos... "
                f"({attempts} intentos restantes)"
            )
            time.sleep(delay_seconds)
    print("❌ No se pudo conectar a la base de datos después de varios intentos.")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

