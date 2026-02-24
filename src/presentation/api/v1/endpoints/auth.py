from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db

from src.presentation.schemas.auth import UserCreate, UserLogin, Token
from src.adapters.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from src.adapters.auth.jwt_auth_adapter import JWTAuthAdapter
from src.application.use_cases.register_user import RegisterUserUseCase
from src.application.use_cases.login_user import LoginUserUseCase

router = APIRouter()


@router.post(
    "/auth/register",
    response_model=Token,
    tags=["Autenticación"],
    status_code=status.HTTP_201_CREATED,
)
def register(user: UserCreate, db: Session = Depends(get_db)):
    user_repo = SQLAlchemyUserRepository(db)
    auth_service = JWTAuthAdapter()
    use_case = RegisterUserUseCase(user_repo, auth_service)
    try:
        return use_case.execute(user)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.post(
    "/auth/login",
    response_model=Token,
    tags=["Autenticación"],
)
def login(user: UserLogin, db: Session = Depends(get_db)):
    user_repo = SQLAlchemyUserRepository(db)
    auth_service = JWTAuthAdapter()
    use_case = LoginUserUseCase(user_repo, auth_service)
    try:
        return use_case.execute(user)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
