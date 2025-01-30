from abc import ABC, abstractmethod

from features.user.domain.email import Email
from features.user.domain.user import User


class UserRepository(ABC):
	@abstractmethod
	async def add(self, user: User):
		pass

	@abstractmethod
	async def get_by_email(self, email: Email) -> User:
		pass
