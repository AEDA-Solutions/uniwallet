from framework import Response as default

class Controller:

	response = default.Response()

	def __init__(self):
		pass

	def define_header(self, label, value):
		pass

	def fetch_response(self, body):
		self.response.body = body
		return self.response

	def bad_response(self):
		self.response.ok = False
		self.response.body = "Resource unavailable"
		return self.response

	def action(self, action_name, variables = None):
		if hasattr(self, action_name) and callable(getattr(self, action_name)):
			return self.fetch_response(getattr(self, action_name)(variables))
		else:
			return self.bad_response()

