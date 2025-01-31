from returns.result import Failure, Result, Success

from features.post.application.post_dto import PostDTO
from features.post.domain.post import Post
from features.shared.domain.valid_string import ValidString
from features.shared.domain.valid_uuid import ValidUUID


class PostMapper:
	@staticmethod
	def to_dto( post: Post ) -> PostDTO:
		return PostDTO( id=post.post_id.value, title=post.title.value,
			content=post.content.value, user_id=post.owner.id.value )

	@staticmethod
	def to_domain( dto: PostDTO ) -> Post:
		return Post.from_primitives( id=dto.id, title=dto.title,
			content=dto.content, user_id=dto.user_id )

	@staticmethod
	def to_dict( post: PostDTO ) -> dict:
		return {
			'id'     : post.id,
			'title'  : post.title,
			'content': post.content,
			'user_id': post.user_id
		}

	@staticmethod
	def from_dict( data: dict ) -> Result[PostDTO, list[str]]:
		errors = []

		id = ValidUUID.from_str( data["id"] )
		if id is None:
			errors.append( 'id' )

		title = ValidString.from_str( data.get( "title" ) )
		if title is None:
			errors.append( 'title' )

		content = ValidString.from_str( data.get( "content" ) )
		if content is None:
			errors.append( 'content' )

		user_id = ValidUUID.from_str( data.get( "user_id" ) )
		if user_id is None:
			errors.append( 'user_id' )

		if errors:
			return Failure( errors )

		return Success(
			PostDTO( id=id.value, title=title.value, content=content.value,
				user_id=user_id.value ) )
