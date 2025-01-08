from pydantic import BaseModel

from features.user.domain.model import User


class UserDTO(BaseModel):
	id: str
	name: str
	email: str

def user_to_dto(user: User) -> UserDTO:
	return UserDTO(id=str(user.id), name=user.name, email=user.email)
