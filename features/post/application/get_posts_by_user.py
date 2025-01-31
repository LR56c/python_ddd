from features.post.domain.post import Post
from features.post.domain.post_dao import PostDAO
from features.shared.domain.valid_uuid import ValidUUID


class GetPostsByUser:
	def __init__(self, dao: PostDAO):
		self.dao = dao

	async def execute(self, user_id : str) -> list[Post]:
		id = ValidUUID.from_str(user_id)
		if not id:
			raise ValueError("Invalid UUID")
		return await self.dao.get_by_user(id)