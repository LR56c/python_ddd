from features.user.application.create_user import CreateUserUseCase
from features.user.domain.model import User
from features.user.domain.repository import UserRepository


class UserService:
	def __init__(self, user_repository: UserRepository):
		self.create_user_use_case = CreateUserUseCase(user_repository)

	def create_user(self, name: str, email: str) -> User:
		return self.create_user_use_case.execute(name=name, email=email)
