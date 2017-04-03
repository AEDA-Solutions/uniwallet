from framework import Controller as std
from app import User as model

class User(std.Controller):
	def __init__(self):
		super().__init__()

	def sample(self, request):
		user = model.User()
		user.foo()
		if 'name' in request.body:
			return request.body['name']
		else:
			return "attribute 'name' not found"

	def abc(self, request):
		user = model.User()
		return "Abc {}".format(user.abc())