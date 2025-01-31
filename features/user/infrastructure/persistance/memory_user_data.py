from typing import List

from returns.result import Failure, Result, Success

from features.user.domain.email import Email
from features.user.domain.user import User
from features.user.domain.user_repository import UserRepository


class MemoryUserData(UserRepository):
	def __init__(self):
		self.users: List[User] = []

	def register(self, user: User ):
		self.users.append(user)

	async def get_user( self, email: Email ) -> Result[User, Exception]:
		return next((Success(user) for user in self.users if user.email.value == email.value), Failure(Exception('User not found')))