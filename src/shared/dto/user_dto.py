from pydantic import BaseModel, EmailStr, Field


class UserCreateDTO(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserLoginDTO(BaseModel):
    email: EmailStr
    password: str


class TokenDTO(BaseModel):
    access_token: str
    token_type: str
    user_name: str
