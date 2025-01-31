import os

from dependency_injector import containers, providers

from api.post.post_instrumentation import PostInstrumentation
from api.post.post_service import PostService
from features.post.application.create_post import CreatePost
from features.post.application.get_posts_by_user import GetPostsByUser
from features.post.infrastructure.persistance.alchemy_post_data import \
	AlchemyPostData

class PostContainer( containers.DeclarativeContainer ):
	wiring_config = containers.WiringConfiguration( modules=[".post_controller"] )
	database = providers.Dependency()
	post_dao = providers.Singleton( AlchemyPostData ,
		session=database
	)
	create = providers.Singleton( CreatePost, dao=post_dao )
	get = providers.Singleton( GetPostsByUser, dao=post_dao )
	post_service = providers.Singleton( PostService, create_post=create,
		get_posts=get, instrumentation=PostInstrumentation() )
