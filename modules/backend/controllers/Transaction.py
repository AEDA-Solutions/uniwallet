from framework import Controller as std

	class Transaction(std.Controller)

		def save(self)
		transaction_id = self.model(data = self.get_request_parameters()).save().last_id()
		return "Done: Transaction {} created successfully".format(transaction_id)