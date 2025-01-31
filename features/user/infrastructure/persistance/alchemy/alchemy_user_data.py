from result import Result
from returns.result import Failure, Success
from sqlalchemy import select

from features.shared.infrastructure.alchemy_database import Session
from features.user.domain.email import Email
from features.user.domain.user import User
from features.user.domain.user_repository import UserRepository
from features.user.infrastructure.persistance.alchemy.user_entity import \
	UserEntity


class AlchemyUserData( UserRepository ):
	def __init__( self ):
		self.session = Session
		print( 'alchemy', self.session )

	async def add( self, user: User ):
		async with Session() as session:
			new_user = UserEntity( id=user.id.value, name=user.name.value, email=user.email.value)
			session.add( new_user )
			await session.commit()

	async def get_by_email( self, email: Email ) -> Result[User, Exception]:
		async with Session() as session:
			result = await session.execute(
				select( UserEntity ).where( UserEntity.email == email.value ) )
			u = result.scalars().first()
			if u is None:
				return Failure(
					Exception( f"User with email {email.value} not found" ) )
			return Success(
				User.from_primitives( u.id, u.name, u.email, u.created_at ) )
