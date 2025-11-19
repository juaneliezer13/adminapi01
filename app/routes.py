from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    get_password_hash,
    verify_password,
)
from app.db.database import get_db
from app.models.user import UserModel
from app.schemas.auth import Token, UserCreate, UserLogin

router = APIRouter()


@router.get("/", tags=["General"], summary="Verificar estado de API")
def read_root():
    """
    Retorna un mensaje simple para verificar que el backend está en línea.
    """
    return {"message": "API Python con PostgreSQL funcionando correctamente"}


@router.post(
    "/auth/register",
    response_model=Token,
    tags=["Autenticación"],
    summary="Registrar nuevo usuario",
    description=(
        "Crea un usuario en la base de datos si el email no existe, "
        "y retorna un token de acceso JWT."
    ),
    status_code=status.HTTP_201_CREATED,
    responses={400: {"description": "El email ya está registrado"}},
)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    hashed_password = get_password_hash(user.password)
    new_user = UserModel(
        email=user.email,
        full_name=user.full_name,
        password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(data={"sub": new_user.email})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_name": new_user.full_name,
    }


@router.post(
    "/auth/login",
    response_model=Token,
    tags=["Autenticación"],
    summary="Iniciar sesión",
    description=(
        "Verifica las credenciales (email y password) y devuelve un token JWT "
        "válido por 1 hora."
    ),
    responses={
        400: {
            "description": (
                "Credenciales incorrectas "
                "(email no encontrado o password erróneo)"
            )
        }
    },
)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    access_token = create_access_token(data={"sub": db_user.email})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_name": db_user.full_name,
    }

