from framework import Controller as std

class User(std.Controller):
	
	def register(self):
		self.model(self.get_request_parameters()).save().close()
		return "Stored motherfucker"

	def update(self):
		self.model(self.get_request_parameters()).save().close()
		return "Stored motherfucka"


