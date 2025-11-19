from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(
        ...,
        min_length=6,
        description="La contraseña debe tener al menos 6 caracteres.",
    )

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Juan Perez",
                "email": "juan@ejemplo.com",
                "password": "password123",
            }
        }


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {"email": "juan@ejemplo.com", "password": "password123"}
        }


class Token(BaseModel):
    access_token: str
    token_type: str
    user_name: str

