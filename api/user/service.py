from api.user.instrumentation import UserInstrumentation
from features.user.application.create_user import CreateUserUseCase
from features.user.domain.model import User
from features.user.domain.repository import UserRepository


class UserService:
	def __init__(self, user_repository: UserRepository, instrumentation : UserInstrumentation):
		print('init UserService')
		self.create_user_use_case = CreateUserUseCase(user_repository)
		self.instrumentation = instrumentation

	async def create_user(self, name: str, email: str) -> User:
		return await self.create_user_use_case.execute(name=name, email=email)
