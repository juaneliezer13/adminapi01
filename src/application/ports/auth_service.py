from abc import ABC, abstractmethod
from typing import Any, Dict


class AuthServicePort(ABC):
    @abstractmethod
    def hash_password(self, plain: str) -> str:
        pass

    @abstractmethod
    def verify_password(self, plain: str, hashed: str) -> bool:
        pass

    @abstractmethod
    def create_access_token(self, data: Dict[str, Any]) -> str:
        pass
