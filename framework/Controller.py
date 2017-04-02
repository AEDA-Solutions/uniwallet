from framework import Response as default

class Controller:

	def __init__(self):
		self.response = default.Response()

	def fetch_response(self, body):
		"""
		fetch_response(): It assigns the response body content and return the Response object
		"""
		self.response.body = body
		return self.response

	def action(self, action_name, variables = None):
		"""
		action(): It tries to call a method called 'action_name' from the current Controller object. Then it returns the output of that method.
		If that method is not found, it returns a warning.
		"""
		if hasattr(self, action_name) and callable(getattr(self, action_name)):
			return self.fetch_response(getattr(self, action_name)(variables))
		else:
			return default.Response().make_warning("Action '{}' unavailable".format(action_name))

