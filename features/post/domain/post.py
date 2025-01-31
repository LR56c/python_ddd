from pydantic import BaseModel

from features.shared.domain.valid_string import ValidString
from features.shared.domain.valid_uuid import ValidUUID


class Post(BaseModel):
	id : ValidUUID
	title : ValidString
	content : ValidString
	user_id : ValidUUID

	@staticmethod
	def create(id: ValidUUID, title: ValidString, content: ValidString, user_id: ValidUUID) -> "Post":
		return Post(id=id, title=title, content=content, user_id=user_id)

	@staticmethod
	def from_primitives(id: str, title: str, content: str, user_id: str) -> "Post":
		return Post(
			id=ValidUUID.from_str(id),
			title=ValidString.from_str(title),
			content=ValidString.from_str(content),
			user_id=ValidUUID.from_str(user_id)
		)