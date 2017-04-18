from framework import Controller as std

class Transaction(std.Controller):
	
	def register(self):
		self.model(self.get_request_parameters()).save().close()
		return "Stored motherfucker"


