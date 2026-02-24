from src.domain.models.user import User
from app.models.user import UserModel
from typing import Optional


def model_to_domain(model: UserModel) -> Optional[User]:
    if not model:
        return None
    return User(
        id=model.id,
        email=model.email,
        full_name=model.full_name,
        password_hash=model.password,
    )


def domain_to_entity(domain: User) -> dict:
    return {
        "id": domain.id,
        "email": domain.email,
        "full_name": domain.full_name,
        "password": domain.password_hash,
    }
