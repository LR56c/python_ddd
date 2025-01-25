import uuid

from features.user.application.dto import UserDTO
from features.user.domain.model import User

class UserMapper:

	@staticmethod
	def to_dto( user: User ) -> UserDTO:
		return UserDTO( id=str( user.id ), name=user.name, email=user.email )


	@staticmethod
	def to_dict( user: UserDTO ) -> dict:
		return {
			'id'   : user.id,
			'name' : user.name,
			'email': user.email
		}

	@staticmethod
	def from_dict( data: dict ) -> UserDTO:
		return UserDTO( id=data['id'], name=data['name'], email=data['email'] )

	@staticmethod
	def to_domain( dto: UserDTO ) -> User:
		return User( id=uuid.UUID( dto.id ), name=dto.name, email=dto.email )