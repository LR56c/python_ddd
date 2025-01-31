from sqlalchemy.ext.asyncio import AsyncSession

from features.post.domain.post import Post
from features.post.domain.post_dao import PostDAO
from features.shared.domain.valid_uuid import ValidUUID
from features.shared.infrastructure.alchemy_database import Session


class AlchemyPostData(PostDAO):
	def __init__(self):
		self.session = Session

	async def add( self, post: Post ):
		pass

	async def update( self, post: Post ):
		pass

	async def remove( self, id: ValidUUID ):
		pass

	async def get_by_user( self, user_id: ValidUUID ) -> list[Post]:
		pass