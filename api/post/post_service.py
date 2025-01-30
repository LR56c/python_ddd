from api.post.post_instrumentation import PostInstrumentation
from features.post.application.post_dto import PostDTO
from features.post.domain.post_dao import PostDAO

class PostService:
	def __init__(self, dao: PostDAO, instrumentation : PostInstrumentation):
		self.dao = dao
		self.instrumentation = instrumentation

	async def create_post(self, dto : PostDTO):
		pass
