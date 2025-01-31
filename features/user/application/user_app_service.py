from abc import ABC, abstractmethod

from features.user.application.user_dto import UserDTO
from features.user.domain.email import Email


class UserAppService(ABC):
	@abstractmethod
	async def register( self, user: UserDTO ):
		pass

	@abstractmethod
	async def get_user( self, email: Email ) -> UserDTO:
		pass
