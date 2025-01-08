from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Body, Depends

from api.user.service import UserService
from api.user.user_container import UserContainer
from pydantic import BaseModel

from features.user.application.dto import UserDTO
from features.user.application.mappers import UserMapper


class CreateUserRequest(BaseModel):
	name: str
	email: str

router = APIRouter()

@router.post("/users", response_model=UserDTO)
@inject
async def create_user(
	name: str = Body(...),
	email: str = Body(...),
	user_service: UserService = Depends(Provide[UserContainer.user_service])
):
	print('create', name, email)
	user = await user_service.create_user(name=name, email=email)
	print('post')
	return UserMapper.user_to_dto(user)