class PasswordTooShortError(Exception):
	"""La contraseña es demasiado corta."""
	pass


class PasswordTooLongError(Exception):
	"""La contraseña es demasiado larga."""
	pass


class PasswordMissingUppercaseError(Exception):
	"""La contraseña debe contener al menos una letra mayúscula."""
	pass


class PasswordMissingLowercaseError(Exception):
	"""La contraseña debe contener al menos una letra minúscula."""
	pass


class PasswordMissingDigitError(Exception):
	"""La contraseña debe contener al menos un dígito."""
	pass


class PasswordMissingSpecialCharacterError(Exception):
	"""La contraseña debe contener al menos un carácter especial."""
	pass