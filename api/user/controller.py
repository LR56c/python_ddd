from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Body, Depends

from api.user.user_service import UserService
from api.user.user_container import UserContainer
from pydantic import BaseModel

from features.user.application.user_dto import UserDTO
from features.user.application.user_mapper import UserMapper


class CreateUserRequest(BaseModel):
	name: str
	email: str

router = APIRouter(prefix='/user', tags=['user'])

@router.post("/", response_model=UserDTO)
@inject
async def create_user(
	user: UserDTO,
	user_service: UserService = Depends(Provide[UserContainer.user_service])
):
	try:
		print('create data:', user)
		await user_service.create_user(user)
		return {
			'result': 'success'
		}
	except Exception as e:
		print('error:', e)
		return {
			'result': 'error'
	}