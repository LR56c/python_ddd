from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Body, Depends

from api.post.post_container import PostContainer
from api.post.post_service import PostService
from features.post.application.post_dto import PostDTO

router = APIRouter(prefix='/post', tags=['post'])

@router.post("/")
@inject
async def create_post(
	post: PostDTO,
	post_service: PostService = Depends(Provide[PostContainer.post_service] )
):
	try:
		await post_service.create(post )
		return {
			'result': 'success'
		}
	except Exception as e:
		print('error:', e)
		return {
			'result': 'error'
	}

@router.get("/{user_id}")
@inject
async def get_posts(
	user_id: str,
	post_service: PostService = Depends(Provide[PostContainer.post_service] )
):
	try:
		posts = await post_service.get_by_user(user_id )
		return {
			'result': 'success',
			'data': posts
		}
	except Exception as e:
		print('error:', e)
		return {
			'result': 'error'
	}