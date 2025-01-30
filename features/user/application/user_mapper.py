from result import Result
from returns.result import Failure, Success

from features.shared.domain.valid_string import ValidString
from features.shared.domain.valid_uuid import ValidUUID
from features.user.application.user_dto import UserDTO
from features.user.domain.email import Email
from features.user.domain.user import User


class UserMapper:

	@staticmethod
	def to_dto( user: User ) -> UserDTO:
		return UserDTO( id=user.id.value, name=user.name.value, email=user.email.value )

	@staticmethod
	def to_dict( user: UserDTO ) -> dict:
		return {
			'id'   : user.id,
			'name' : user.name,
			'email': user.email
		}

	@staticmethod
	def from_dict( data: dict ) -> Result[UserDTO, list[str]]:
		errors = []

		id = ValidUUID.from_str(data.get( "id" ))
		if id is None:
			errors.append( 'id' )

		name = ValidString.from_str(data.get( "name" ))
		if name is None:
			errors.append( 'name' )

		email = Email.from_str(data.get( "email" ))
		if email is None:
			errors.append( 'email' )

		if errors:
			return Failure(errors)

		return Success(UserDTO( id=id.value, name=name.value, email=email.value ))


