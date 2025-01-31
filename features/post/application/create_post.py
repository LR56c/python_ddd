from features.post.application.post_dto import PostDTO
from features.post.application.post_mapper import PostMapper
from features.post.domain.post_dao import PostDAO


class CreatePost:
	def __init__(self, dao: PostDAO):
		self.dao = dao

	async def execute(self, dto : PostDTO):
		post = PostMapper.to_domain(dto)
		await self.dao.add(post)