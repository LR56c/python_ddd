from returns.pipeline import is_successful

from features.shared.domain.valid_string import ValidString
from features.shared.domain.valid_uuid import ValidUUID
from features.user.application.user_dto import UserDTO
from features.user.domain.email import Email
from features.user.domain.user import User
from features.user.domain.user_repository import UserRepository


class CreateUser:
	def __init__(self, repo: UserRepository):
		self.repo = repo

	async def execute(self, dto : UserDTO):
		email = Email.from_str(dto.email)
		if email is None:
			raise ValueError("Invalid email.")

		existing_user = await self.repo.get_by_email(email)
		if is_successful(existing_user):
			raise ValueError("Email already exists.")

		errors = []
		id = ValidUUID.from_str(dto.id)
		if id is None:
			errors.append('id')

		name = ValidString.from_str(dto.name)
		if name is None:
			errors.append('name')

		if errors:
			raise ValueError(f"Invalid user data: {', '.join(errors)}")

		user = User.create(id, name, email)
		await self.repo.add(user)
