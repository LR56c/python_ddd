import logging

class UserInstrumentation:
	def __init__(self, logger_name: str = "user_instrumentation"):
		self.logger = logging.getLogger(logger_name)

	def log_info(self, message: str):
		self.logger.info(message)

	def log_error(self, message: str):
		self.logger.error(message)
