from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Body, Depends

from api.user.user_service import UserService
from api.user.user_container import UserContainer

from features.user.application.user_dto import UserDTO

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