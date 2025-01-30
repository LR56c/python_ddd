from abc import ABC, abstractmethod

from features.post.domain.post import Post
from features.shared.domain.valid_uuid import ValidUUID


class PostDAO(ABC):
	@abstractmethod
	async def add(self, post : Post):
		pass

	@abstractmethod
	async def update(self, post : Post):
		pass

	@abstractmethod
	async def remove(self, id : ValidUUID):
		pass

	@abstractmethod
	async def get_by_user(self, user_id : ValidUUID) -> list[Post]:
		pass
