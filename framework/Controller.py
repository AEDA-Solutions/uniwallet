from framework import Response as default

class Controller:

	def __init__(self):
		pass

	def define_header(self, label, value):
		pass

	def fetch_response(self, body):
		response = default.Response()
		response.body = body
		return response

	def action(self, action_name, variables = None):
		if hasattr(self, action_name) and callable(getattr(self, action_name)):
			return self.fetch_response(getattr(self, action_name)(variables))
		else:
			return default.Response().make_warning("Resource unavailable")

