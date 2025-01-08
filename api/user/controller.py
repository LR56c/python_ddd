from fastapi import APIRouter, Body, Depends

from api.app_container import AppContainer
from features.user.application.mappers import user_to_dto, UserDTO
from features.user.application.service import UserService
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
	name: str
	email: str

router = APIRouter()

def get_user_service() -> UserService:
	return AppContainer.user.user_service()

@router.post("/users", response_model=UserDTO)
def create_user(
	name: str = Body(...),
	email: str = Body(...),
):
	print('create', name, email)
	user = get_user_service().create_user(name=name, email=email)
	print('post')
	return user_to_dto(user)