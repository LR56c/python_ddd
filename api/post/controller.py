from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

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