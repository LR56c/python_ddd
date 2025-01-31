from api.user.user_instrumentation import UserInstrumentation
from features.user.application.create_user import CreateUser
from features.user.application.user_dto import UserDTO


class UserService:
	def __init__(self, create_user: CreateUser, instrumentation : UserInstrumentation):
		self.create_user = create_user
		self.instrumentation = instrumentation

	async def create(self, dto : UserDTO):
		await self.create_user.execute(dto )

