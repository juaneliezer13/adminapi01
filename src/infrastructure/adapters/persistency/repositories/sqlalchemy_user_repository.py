from src.application.ports.user_repository import UserRepositoryPort
from src.domain.models.user import User
from app.models.user import UserModel
from sqlalchemy.orm import Session
from src.infrastructure.adapters.persistency.entity_mappers.user_mapper import model_to_domain


class SQLAlchemyUserRepository(UserRepositoryPort):
    def __init__(self, session: Session):
        self.session = session

    def add(self, user: User) -> User:
        model = UserModel(email=user.email, full_name=user.full_name, password=user.password_hash)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model_to_domain(model)

    def find_by_email(self, email: str) -> User | None:
        model = self.session.query(UserModel).filter(UserModel.email == email).first()
        return model_to_domain(model)

    def list_all(self) -> list[User]:
        models = self.session.query(UserModel).all()
        return [model_to_domain(m) for m in models]
