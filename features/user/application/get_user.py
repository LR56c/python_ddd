from result import Result
from returns.result import Failure, Success

from features.user.domain.email import Email
from features.user.domain.user import User
from features.user.domain.user_repository import UserRepository


class GetUser:
	def __init__( self, repo: UserRepository ):
		self.repo = repo

	async def execute( self, email: str ) -> Result[User, Exception]:
		e = Email.from_str( email )
		if e is None:
			return Failure( Exception( "Invalid email" ) )

		return Success(await self.repo.get_user( e ))

