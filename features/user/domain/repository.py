from abc import ABC, abstractmethod

from features.user.domain.model import User


class UserRepository(ABC):
	@abstractmethod
	async def add(self, user: User) -> User:
		pass

	@abstractmethod
	async def get_by_email(self, email: str) -> User:
		pass
