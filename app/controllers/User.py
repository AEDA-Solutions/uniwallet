from framework import Controller as default

class User(default.Controller):
	def __init__(self):
		pass

	def sample(self, variables = None):
		return "hello bitch: {}".format(repr(variables.POST))