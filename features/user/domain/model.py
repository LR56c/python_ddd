from pydantic import BaseModel
from uuid import UUID, uuid4

class User(BaseModel):
	id: UUID
	name: str
	email: str

	@staticmethod
	def create(name: str, email: str) -> "User":
		return User(id=uuid4(), name=name, email=email)
