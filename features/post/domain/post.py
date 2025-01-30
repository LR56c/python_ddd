from pydantic import BaseModel

from features.shared.domain.valid_string import ValidString
from features.shared.domain.valid_uuid import ValidUUID
from features.user.domain.user import User


class Post(BaseModel):
	id : ValidUUID
	title : ValidString
	content : ValidString
	owner : User