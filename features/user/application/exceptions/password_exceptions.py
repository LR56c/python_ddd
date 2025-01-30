class PasswordException(Exception):
	pass

class PasswordTooShortError(PasswordException):
	"""La contraseña es demasiado corta."""
	pass


class PasswordTooLongError(PasswordException):
	"""La contraseña es demasiado larga."""
	pass


class PasswordMissingUppercaseError(PasswordException):
	"""La contraseña debe contener al menos una letra mayúscula."""
	pass


class PasswordMissingLowercaseError(PasswordException):
	"""La contraseña debe contener al menos una letra minúscula."""
	pass


class PasswordMissingDigitError(PasswordException):
	"""La contraseña debe contener al menos un dígito."""
	pass


class PasswordMissingSpecialCharacterError(PasswordException):
	"""La contraseña debe contener al menos un carácter especial."""
	pass