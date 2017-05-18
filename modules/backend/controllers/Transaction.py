from framework import Controller as std

	class Transaction(std.Controller)

		def sucess(self)
		pass

		def failure(self)

		def save(self)
		transaction_id = self.model(self.get_request_parameters()).save().last_id()
		return "Done: Transaction {} created successfully".format(last_id)