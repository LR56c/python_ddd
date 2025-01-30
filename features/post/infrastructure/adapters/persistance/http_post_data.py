from features.post.application.post_app_service import PostAppService
from features.post.application.post_dto import PostDTO
from features.shared.domain.valid_uuid import ValidUUID


class HttpPostData(PostAppService):
	async def add( self, post: PostDTO ):
		pass

	async def update( self, post: PostDTO ):
		pass

	async def remove( self, id: ValidUUID ):
		pass

	async def get_by_user( self, user_id: ValidUUID ) -> list[PostDTO]:
		pass