from api.post.post_instrumentation import PostInstrumentation
from features.post.application.create_post import CreatePost
from features.post.application.get_posts_by_user import GetPostsByUser
from features.post.application.post_dto import PostDTO
from features.post.application.post_mapper import PostMapper

class PostService:
	def __init__(self, create_post : CreatePost, get_posts : GetPostsByUser, instrumentation : PostInstrumentation):
		self.create_post = create_post
		self.get_posts = get_posts
		self.instrumentation = instrumentation

	async def create(self, dto : PostDTO):
		await self.create_post.execute(dto)

	async def get_by_user(self, user_id : str) -> list[PostDTO]:
		posts_domain = await self.get_posts.execute(user_id)
		posts_dto = [PostMapper.to_dto(post) for post in posts_domain]
		return posts_dto
