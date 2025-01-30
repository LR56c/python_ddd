from pydantic import BaseModel

from features.shared.domain.valid_datetime import ValidDateTime
from features.shared.domain.valid_string import ValidString
from features.shared.domain.valid_uuid import ValidUUID
from features.user.domain.email import Email


class User(BaseModel):
	id: ValidUUID
	name: ValidString
	email: Email
	created_at : ValidDateTime

	@staticmethod
	def create(id : ValidUUID, name: ValidString, email: Email) -> "User":
		return User(id=id, name=name, email=email, created_at=ValidDateTime.now())


	@staticmethod
	def from_primitives(id: str, name: str, email: str, created_at: str) -> "User":
		return User(
			id=ValidUUID.from_str(id),
			name=ValidString.from_str(name),
			email=Email.from_str(email),
			created_at=ValidDateTime.from_str(created_at)
		)