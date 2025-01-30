import os

from dependency_injector import containers, providers

from api.user.user_instrumentation import UserInstrumentation
from api.user.user_service import UserService
from features.user.application.create_user import CreateUser
from features.user.infrastructure.persistance.alchemy.alchemy_user_data import \
	AlchemyUserData


class UserContainer( containers.DeclarativeContainer ):
	wiring_config = containers.WiringConfiguration( modules=[".controller"] )
	# username = os.getenv('MONGO_INITDB_ROOT_USERNAME')
	# password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
	# host = os.getenv('MONGO_HOST')
	# url = f'mongodb://{username}:{password}@{host}/?authSource=admin'
	# client = providers.Resource( AsyncIOMotorClient, url )
	# user_repository = providers.Singleton(FakeUserData)
	# user_repository = providers.Singleton( MongoUserData, client=client )
	session = providers.Dependency()
	user_repository = providers.Singleton( AlchemyUserData, session=session )
	create = CreateUser(repo=user_repository)
	user_service = providers.Singleton( UserService,
		create_user=create, instrumentation=UserInstrumentation() )
