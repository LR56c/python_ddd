import uuid
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class ValidUUID( BaseModel ):
	value: str

	@staticmethod
	def create() -> "ValidUUID":
		return ValidUUID( value=str( uuid4() ) )

	@staticmethod
	def from_str( value: str ) -> Optional["ValidUUID"]:
		try:
			return ValidUUID( value=str(UUID(value)) )
		except:
			return None
