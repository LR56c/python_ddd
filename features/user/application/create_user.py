from features.user.domain.model import User
from features.user.domain.repository import UserRepository


class CreateUserUseCase:
	def __init__(self, user_repository: UserRepository):
		self.user_repository = user_repository

	async def execute(self, name: str, email: str) -> User:
		existing_user = await self.user_repository.get_by_email(email)
		if existing_user:
			raise ValueError("User with this email already exists.")

		user = User.create(name=name, email=email)
		return await self.user_repository.add(user)
