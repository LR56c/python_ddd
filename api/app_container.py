from dependency_injector import containers, providers

from api.post.post_container import PostContainer
from api.user.user_container import UserContainer
from features.shared.infrastructure.alchemy_database import get_alchemy_session


class AppContainer( containers.DeclarativeContainer ):
	database = providers.Resource(get_alchemy_session )
	user_container = providers.Container( UserContainer,
		database=database
	)
	post_container = providers.Container( PostContainer,
		database=database
	)
