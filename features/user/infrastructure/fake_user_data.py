from typing import List

from features.user.domain.model import User
from features.user.domain.repository import UserRepository


class FakeUserData(UserRepository):
	def __init__(self):
		self.users: List[User] = []

	def add(self, user: User) -> User:
		self.users.append(user)
		return user

	def get_by_email(self, email: str) -> User:
		return next((user for user in self.users if user.email == email), None)
