from dependency_injector import containers, providers

from features.user.application.service import UserService
from features.user.infrastructure.fake_user_data import FakeUserData


class UserContainer(containers.DeclarativeContainer):
	user_repository = providers.Singleton(FakeUserData)
	user_service = providers.Factory(UserService, user_repository=user_repository)
