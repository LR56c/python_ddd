import os

from dependency_injector import containers, providers

from api.user.user_instrumentation import UserInstrumentation
from api.user.user_service import UserService
from features.user.application.create_user import CreateUser
from features.user.domain.email import Email
from features.user.domain.user_repository import UserRepository
from features.user.infrastructure.persistance.alchemy.alchemy_user_data import \
	AlchemyUserData
from features.user.infrastructure.persistance.memory_user_data import \
	MemoryUserData


class UserContainer( containers.DeclarativeContainer ):
	wiring_config = containers.WiringConfiguration( modules=[".controller"] )
	# username = os.getenv('MONGO_INITDB_ROOT_USERNAME')
	# password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
	# host = os.getenv('MONGO_HOST')
	# url = f'mongodb://{username}:{password}@{host}/?authSource=admin'
	# client = providers.Resource( AsyncIOMotorClient, url )
	# user_repository = providers.Singleton( MongoUserData, client=client )
	# user_repository : UserRepository = providers.Singleton( AlchemyUserData )
	user_repository = providers.Singleton(AlchemyUserData)
	create = providers.Singleton(CreateUser,
		repo=user_repository
	)
	user_service = providers.Singleton( UserService,
		create_user=create, instrumentation=UserInstrumentation() )
