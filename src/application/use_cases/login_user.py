from src.application.ports.user_repository import UserRepositoryPort
from src.application.ports.auth_service import AuthServicePort
from src.shared.dto.user_dto import UserLoginDTO, TokenDTO


class LoginUserUseCase:
    def __init__(self, user_repo: UserRepositoryPort, auth_service: AuthServicePort):
        self.user_repo = user_repo
        self.auth_service = auth_service

    def execute(self, login: UserLoginDTO) -> TokenDTO:
        user = self.user_repo.find_by_email(login.email)
        if not user:
            raise ValueError("Credenciales incorrectas")
        if not self.auth_service.verify_password(login.password, user.password_hash):
            raise ValueError("Credenciales incorrectas")

        access_token = self.auth_service.create_access_token({"sub": user.email})
        return TokenDTO(access_token=access_token, token_type="bearer", user_name=user.full_name)
