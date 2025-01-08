import os

from dependency_injector import containers, providers
from motor.motor_asyncio import AsyncIOMotorClient

from api.user.instrumentation import UserInstrumentation
from api.user.service import UserService
from features.user.infrastructure.mongo_user_data import MongoUserData


class UserContainer( containers.DeclarativeContainer ):
	wiring_config = containers.WiringConfiguration( modules=[".controller"] )
	username = os.getenv('MONGO_INITDB_ROOT_USERNAME')
	password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
	host = os.getenv('MONGO_HOST')
	url = f'mongodb://{username}:{password}@{host}/?authSource=admin'
	client = providers.Resource( AsyncIOMotorClient, url )
	# user_repository = providers.Singleton(FakeUserData)
	user_repository = providers.Singleton( MongoUserData, client=client )
	user_service = providers.Singleton( UserService,
		user_repository=user_repository, instrumentation=UserInstrumentation() )
