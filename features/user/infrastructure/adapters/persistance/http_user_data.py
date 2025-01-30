from features.shared.domain.valid_uuid import ValidUUID
from features.user.application.user_app_service import UserAppService
from features.user.application.user_dto import UserDTO


class HttpUserData(UserAppService):
	async def add( self, user: UserDTO ):
		pass

	async def get_by_id( self, id: ValidUUID ) -> UserDTO:
		pass