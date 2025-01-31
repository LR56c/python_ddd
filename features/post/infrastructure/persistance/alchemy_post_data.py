from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from features.post.domain.post import Post
from features.post.domain.post_dao import PostDAO
from features.post.infrastructure.persistance.post_entity import PostEntity
from features.shared.domain.valid_uuid import ValidUUID


class AlchemyPostData( PostDAO ):
	def __init__( self, session : AsyncSession ):
		self.session = session

	async def add( self, post: Post ):
		async with self.session as session:
			new_post = PostEntity( id=post.id.value, title=post.title.value,
				content=post.content.value, user_id=post.user_id.value )
			session.add( new_post )
			await session.commit()

	async def update( self, post: Post ):
		pass

	async def remove( self, id: ValidUUID ):
		pass

	async def get_by_user( self, user_id: ValidUUID ) -> list[Post]:
		async with self.session as session:
			result = await session.execute(
				select( PostEntity ).where( PostEntity.user_id == user_id.value ) )
			database_posts = result.scalars().all()
			domain_posts = []
			for post in database_posts:
				# print('database entry', post.id, post.title, post.content,post.user_id)
				domain_posts.append(
					Post.from_primitives( str(post.id), post.title, post.content,
						str(post.user_id) ) )
			return domain_posts
