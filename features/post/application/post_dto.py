from pydantic import BaseModel

class PostDTO(BaseModel):
		id: str
		title: str
		content: str
		# user : UserDTO
		user_id : str