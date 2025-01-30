from typing import Optional

from pydantic import BaseModel


class ValidString( BaseModel ):
	value: str

	@staticmethod
	def from_str( value: str ) -> Optional["ValidString"]:
		if not value:
			return None
		return ValidString( value=value )
