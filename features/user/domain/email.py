from typing import Optional

from pydantic import BaseModel

from email_validator import validate_email, EmailNotValidError


class Email( BaseModel ):
	value: str

	@staticmethod
	def from_str( value: str, checker: bool = False ) -> Optional["Email"]:
		try:
			emailinfo = validate_email( value, check_deliverability=checker )
			return Email( value=emailinfo.normalized )
		except EmailNotValidError as e:
			return None
