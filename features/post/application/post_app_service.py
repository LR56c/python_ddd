from abc import ABC, abstractmethod

from features.post.application.post_dto import PostDTO
from features.shared.domain.valid_uuid import ValidUUID


class PostAppService(ABC):
	@abstractmethod
	async def add(self, post : PostDTO):
		pass

	@abstractmethod
	async def update(self, post : PostDTO):
		pass

	@abstractmethod
	async def remove(self, id : ValidUUID):
		pass

	@abstractmethod
	async def get_by_user(self, user_id : ValidUUID) -> list[PostDTO]:
		pass
