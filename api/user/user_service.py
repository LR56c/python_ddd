from returns.pipeline import is_successful

from api.user.user_instrumentation import UserInstrumentation
from features.user.application.create_user import CreateUser
from features.user.application.get_user import GetUser
from features.user.application.user_dto import UserDTO
from features.user.application.user_mapper import UserMapper


class UserService:
	def __init__(self, create_user: CreateUser, get_user : GetUser, instrumentation : UserInstrumentation):
		self.create_user = create_user
		self.get_user = get_user
		self.instrumentation = instrumentation
		print('user service:', self.create_user, self.get_user, self.instrumentation)

	async def create(self, dto : UserDTO):
		await self.create_user.execute(dto )

	async def get_user_by_email(self, email : str ) -> UserDTO:
		u =  await self.get_user.execute(email)

		if is_successful(u):
			return UserMapper.to_dto(u.unwrap())
		else:
			raise Exception("User not found")

