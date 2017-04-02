from framework import Controller as default

class User(default.Controller):
	def __init__(self):
		super().__init__()

	def sample(self, request = None):
		if 'name' in request.body:
			return request.body['name']
		else:
			return "attribute 'name' not found"