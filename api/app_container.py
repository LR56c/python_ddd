from dependency_injector import containers, providers

from api.post.post_container import PostContainer
from api.user.user_container import UserContainer


class AppContainer( containers.DeclarativeContainer ):
	user_container = providers.Container( UserContainer )
	post_container = providers.Container( PostContainer )
