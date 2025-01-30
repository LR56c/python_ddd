from sqlalchemy.ext.asyncio import AsyncSession

from features.user.domain.email import Email
from features.user.domain.user import User
from features.user.domain.user_repository import UserRepository


class AlchemyUserData(UserRepository):
	def __init__(self, session : AsyncSession):
		self.session = session

	async def add( self, user: User ):
		pass

	async def get_by_email( self, email: Email ) -> User:
		pass