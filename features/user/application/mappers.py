import uuid

from features.user.application.dto import UserDTO
from features.user.domain.model import User

class UserMapper:

	@staticmethod
	def user_to_dto( user: User ) -> UserDTO:
		return UserDTO( id=str( user.id ), name=user.name, email=user.email )


	@staticmethod
	def dto_to_user( dto: UserDTO ) -> User:
		return User( id=uuid.UUID( dto.id ), name=dto.name, email=dto.email )
