from dependency_injector import containers

from features.user.dependencies_container import UserContainer


class AppContainer(containers.DeclarativeContainer):
	user = UserContainer()
	userabc = UserContainer()
