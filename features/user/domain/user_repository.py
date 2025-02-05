from abc import ABC, abstractmethod

from returns.result import Result

from features.user.domain.email import Email
from features.user.domain.user import User


class UserRepository(ABC):
	@abstractmethod
	async def register(self, user: User ):
		pass

	@abstractmethod
	async def get_user(self, email: Email ) -> Result[User, Exception]:
		pass
