from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine, wait_for_db
from app.routes import router as api_router

# --- INITIAL SETUP ---
wait_for_db()
Base.metadata.create_all(bind=engine)

# --- DEFINICIÓN DE METADATA PARA SWAGGER ---
tags_metadata = [
    {
        "name": "Autenticación",
        "description": "Endpoints para el **registro** e **inicio de sesión** de usuarios.",
    },
    {
        "name": "General",
        "description": "Verificación de estado de la API.",
    },
]

# --- SETUP FASTAPI CON DOCS ---
app = FastAPI(
    title="API de Autenticación Vue+FastAPI",
    description="Backend ligero para manejar usuarios con PostgreSQL y JWT.",
    version="1.0.0",
    openapi_tags=tags_metadata,
    docs_url="/docs",  # URL de Swagger UI
    redoc_url="/redoc",  # URL de ReDoc
)

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ROUTES ---
app.include_router(api_router)

