from dataclasses import dataclass
import re

from features.user.domain.exceptions.password_exceptions import *


@dataclass( frozen=True )
class Password:
	value: str

	def __post_init__( self ):
		self._validate()

	def _validate( self ):
		if len( self.value ) < 8:
			raise PasswordTooShortError(
				"La contraseña debe tener al menos 8 caracteres." )
		if len( self.value ) > 128:
			raise PasswordTooLongError(
				"La contraseña no puede tener más de 128 caracteres." )
		if not any( char.isupper() for char in self.value ):
			raise PasswordMissingUppercaseError(
				"La contraseña debe contener al menos una letra mayúscula." )
		if not any( char.islower() for char in self.value ):
			raise PasswordMissingLowercaseError(
				"La contraseña debe contener al menos una letra minúscula." )
		if not any( char.isdigit() for char in self.value ):
			raise PasswordMissingDigitError(
				"La contraseña debe contener al menos un dígito." )
		if not re.search( r"[!@#$%^&*(),.?\":{}|<>]", self.value ):
			raise PasswordMissingSpecialCharacterError(
				"La contraseña debe contener al menos un carácter especial (!@#$%^&*("
				"),.?\":{}|<>)." )

	def strength( self ) -> str:
		"""Evalúa la fortaleza de la contraseña."""
		length = len( self.value )
		score = sum( [bool( re.search( r'[A-Z]', self.value ) ),
			bool( re.search( r'[a-z]', self.value ) ),
			bool( re.search( r'\d', self.value ) ),
			bool( re.search( r'[!@#$%^&*(),.?":{}|<>]', self.value ) ), ] )
		if length > 12 and score == 4:
			return "Fuerte"
		elif length >= 8 and score >= 3:
			return "Moderada"
		else:
			return "Débil"
