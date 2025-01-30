from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ValidDateTime( BaseModel ):
	value: datetime

	@staticmethod
	def now() -> "ValidDateTime":
		return ValidDateTime( value=datetime.now() )

	@staticmethod
	def create( value: datetime ) -> Optional["ValidDateTime"]:
		if isinstance( value, datetime ):
			return ValidDateTime( value=value )
		return None

	@staticmethod
	def from_str( value: str ) -> Optional["ValidDateTime"]:
		try:
			return ValidDateTime( value=datetime.fromisoformat( value ) )
		except:
			return None
