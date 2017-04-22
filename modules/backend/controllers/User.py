from framework import Controller as std

class User(std.Controller):
	
	def register(self):
		return "Done: {} is the last id created".format(self.model(self.get_request_parameters()).save())

	def update(self):
		return "Done: {} rows affected".format(self.model(self.get_request_parameters()).save())

	def doit(self):
		return self.request.parameters;

	def make(self):
		return "Making makers"

	def foo(self):
		return "Hello world"


