import os

from dependency_injector import containers, providers

from api.post.post_instrumentation import PostInstrumentation
from api.post.post_service import PostService
from features.user.infrastructure.persistance.alchemy.alchemy_user_data import \
	AlchemyUserData


class PostContainer( containers.DeclarativeContainer ):
	wiring_config = containers.WiringConfiguration( modules=[".controller"] )
	post_dao = providers.Singleton( AlchemyUserData )
	post_service = providers.Singleton( PostService, dao=post_dao,
		instrumentation=PostInstrumentation() )
