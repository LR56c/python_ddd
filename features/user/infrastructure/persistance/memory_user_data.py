from typing import List

from features.user.domain.email import Email
from features.user.domain.user import User
from features.user.domain.user_repository import UserRepository


class MemoryUserData(UserRepository):
	def __init__(self):
		self.users: List[User] = []

	def add(self, user: User):
		self.users.append(user)

	def get_by_email(self, email: Email) -> User:
		return next((user for user in self.users if user.email == email.value), None)
