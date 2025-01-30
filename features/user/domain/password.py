import re

from pydantic import BaseModel
from returns.result import Failure, Result, Success

from features.user.application.exceptions.password_exceptions import \
	PasswordException
from features.user.domain.exceptions.password_exceptions import *


class Password(BaseModel):
	value: str

	@staticmethod
	def create( value: str ) -> Result["Password", list[PasswordException]]:
		errors = []
		if len( value ) < 8:
			errors.append( PasswordTooShortError(
				"La contraseña debe tener al menos 8 caracteres." ) )
		if len( value ) > 128:
			errors.append( PasswordTooLongError(
				"La contraseña no puede tener más de 128 caracteres." ) )
		if not any( char.isupper() for char in value ):
			errors.append( PasswordMissingUppercaseError(
				"La contraseña debe contener al menos una letra mayúscula." ) )
		if not any( char.islower() for char in value ):
			errors.append( PasswordMissingLowercaseError(
				"La contraseña debe contener al menos una letra minúscula." ) )
		if not any( char.isdigit() for char in value ):
			errors.append( PasswordMissingDigitError(
				"La contraseña debe contener al menos un dígito." ) )
		if not re.search( r"[!@#$%^&*(),.?\":{}|<>]", value ):
			errors.append( PasswordMissingSpecialCharacterError(
				"La contraseña debe contener al menos un carácter especial (!@#$%^&*("
				"),.?\":{}|<>)." ) )

		if errors:
			return Failure( errors )

		return Success( Password( value ) )

	@staticmethod
	def strength( value: str ) -> str:
		length = len( value )
		score = sum( [bool( re.search( r'[A-Z]', value ) ),
			bool( re.search( r'[a-z]', value ) ), bool( re.search( r'\d', value ) ),
			bool( re.search( r'[!@#$%^&*(),.?":{}|<>]', value ) ), ] )
		if length > 12 and score == 4:
			return "high"
		elif length >= 8 and score >= 3:
			return "medium"
		else:
			return "low"
