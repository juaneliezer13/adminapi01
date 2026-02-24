from src.ports.auth_service import AuthServicePort
from typing import Any, Dict
from app.core.security import create_access_token, get_password_hash, verify_password


class JWTAuthAdapter(AuthServicePort):
    def hash_password(self, plain: str) -> str:
        return get_password_hash(plain)

    def verify_password(self, plain: str, hashed: str) -> bool:
        return verify_password(plain, hashed)

    def create_access_token(self, data: Dict[str, Any]) -> str:
        return create_access_token(data=data)
