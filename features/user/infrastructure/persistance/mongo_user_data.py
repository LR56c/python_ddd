from motor.motor_asyncio import AsyncIOMotorClient

from features.user.domain.user import User
from features.user.domain.user_repository import UserRepository


class MongoUserData( UserRepository ):
	def __init__( self, client : AsyncIOMotorClient ):
		self.client = client

	async def add( self, user: User ) -> User:
		return user

	async def get_by_email( self, email: str ) -> User:
		# db = self.client.get_database( 'notification' )
		# collection = db.get_collection( 'notification' )
		# await collection.insert_one( { 'name': 'test' } )
		# users = collection.find()
		#
		# async for user in users:
		# 	print('e',user)
		return None
