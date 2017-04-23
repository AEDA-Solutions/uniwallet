from framework import Controller as std

class Transaction(std.Controller):
	
	def save(self):
		self.model(self.get_request_parameters()).save().close()
		return "Transaction sucessful"
