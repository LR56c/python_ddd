import os

from dependency_injector import containers, providers

from api.post.post_container import PostContainer
from api.user.user_container import UserContainer
from features.shared.infrastructure.alchemy_database import Session


class AppContainer( containers.DeclarativeContainer ):
	session = providers.Resource( Session)
	user_container = providers.Container( UserContainer,
		session=session
	)
	post_container = providers.Container( PostContainer,
		session=session
	)
