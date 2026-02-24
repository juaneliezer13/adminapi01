from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.models.user import User


class UserRepositoryPort(ABC):
    @abstractmethod
    def add(self, user: User) -> User:
        """Persists a User and returns the saved entity."""

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        """Returns a User by email or None if not found."""

    @abstractmethod
    def list_all(self) -> List[User]:
        """Return a list with all users (domain objects)."""
