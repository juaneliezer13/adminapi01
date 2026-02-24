from fastapi import APIRouter
from src.presentation.api.v1.endpoints import auth as auth_endpoints, export as export_endpoints

api_router = APIRouter()
api_router.include_router(auth_endpoints.router)
api_router.include_router(export_endpoints.router)
