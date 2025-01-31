from result import Result
from returns.result import Failure, Success
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from features.user.domain.email import Email
from features.user.domain.user import User
from features.user.domain.user_repository import UserRepository
from features.user.infrastructure.persistance.alchemy.user_entity import \
	UserEntity


class AlchemyUserData( UserRepository ):
	def __init__( self, session : AsyncSession ):
		self.session = session

	async def register( self, user: User ):
		async with self.session as session:
			new_user = UserEntity( id=user.id.value, name=user.name.value, email=user.email.value)
			session.add( new_user )
			await session.commit()

	async def get_user( self, email: Email ) -> Result[User, Exception]:
		async with self.session as session:
			result = await session.execute(
				select( UserEntity ).where( UserEntity.email == email.value ) )
			u = result.scalars().first()
			if u is None:
				return Failure(
					Exception( f"User with email {email.value} not found" ) )
			return Success(
				User.from_primitives( u.id, u.name, u.email, u.created_at ) )
