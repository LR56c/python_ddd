from features.user.application.user_app_service import UserAppService
from features.user.application.user_dto import UserDTO
from features.user.domain.email import Email


class HttpUserData(UserAppService):
	async def register( self, user: UserDTO ):
		pass

	async def get_user( self, email: Email ) -> UserDTO:
		pass