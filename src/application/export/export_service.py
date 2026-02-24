from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.user import User


class ExportServicePort(ABC):
    @abstractmethod
    def export_users_csv(self, users: List[User]) -> bytes:
        """Returns a CSV bytes payload with users."""
