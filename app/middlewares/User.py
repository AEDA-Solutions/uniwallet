from framework import Middleware as std

class User(std.Middleware):

	def __init__(self):
		super().__init__()

	def authorized(self):
		return ["client", "manager"]

	def validate(self):
		return {
			"name": ["required", "email"],
			"email": ["required", "email"],
			"age": ["required", "integer"],
			"addr": ["optional"]
		}