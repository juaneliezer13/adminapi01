from src.application.ports.user_repository import UserRepositoryPort
from src.application.ports.auth_service import AuthServicePort
from src.shared.dto.user_dto import UserCreateDTO, TokenDTO
from src.domain.models.user import User


class RegisterUserUseCase:
    def __init__(self, user_repo: UserRepositoryPort, auth_service: AuthServicePort):
        self.user_repo = user_repo
        self.auth_service = auth_service

    def execute(self, user_create: UserCreateDTO) -> TokenDTO:
        existing = self.user_repo.find_by_email(user_create.email)
        if existing:
            raise ValueError("El email ya está registrado")

        hashed = self.auth_service.hash_password(user_create.password)
        user = User(id=None, email=user_create.email, full_name=user_create.full_name, password_hash=hashed)
        saved = self.user_repo.add(user)

        access_token = self.auth_service.create_access_token({"sub": saved.email})
        return TokenDTO(access_token=access_token, token_type="bearer", user_name=saved.full_name)
