from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Body, Depends

from api.user.user_service import UserService
from api.user.user_container import UserContainer
from features.shared.domain.valid_uuid import ValidUUID

from features.user.application.user_dto import UserDTO
from features.user.domain.email import Email

router = APIRouter(prefix='/user', tags=['user'])

@router.post("/")
@inject
async def create_user(
	user: UserDTO,
	user_service: UserService = Depends(Provide[UserContainer.user_service])
):
	try:
		await user_service.create(user)
		return {
			'result': 'success'
		}
	except Exception as e:
		print('error:', e)
		return {
			'result': 'error'
	}

@router.get( "/{email}" )
@inject
async def create_user( email: str, user_service: UserService = Depends(
	Provide[UserContainer.user_service] ) ):
	try:
		user = await user_service.get_user_by_email( email )
		return {
			'result': 'success',
			'data'  : user
		}
	except Exception as e:
		print( 'error:', e )
		return {
			'result': 'error'
		}