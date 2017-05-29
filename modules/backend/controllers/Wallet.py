from framework import Controller as std

class Wallet(std.Controller):

	def register(self):
		wallet_id = self.model(data = self.get_request_parameters()).save().last_id()
		return "Done: Wallet {} created successfully".format(wallet_id)

