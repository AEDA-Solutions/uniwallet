from framework import Controller as std

class User(std.Controller):
	
	def register(self):
		return "Done: {} is the last id created".format(self.model(self.get_request_parameters()).save().last_id())

	def update(self):
		return "Done: {} rows affected".format(self.model(self.get_request_parameters()).save().count_rows())

	def delete(self):
		return "Done: {} rows affected".format(self.model().destroy(list({'id': item} for item in self.get_request_parameters()['ids'])).count_rows())

	def fetch(self):
		return self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit')).fetch(fields_to_ignore = ['password'])

	def doit(self):
		return self.request.parameters

	def make(self):
		return "Making makers"

	def foo(self):
		return "Hello world"


