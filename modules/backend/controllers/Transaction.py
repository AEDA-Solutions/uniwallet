from framework import Controller as std

	class Transaction(std.Controller)

		def pending(self)
		if self.model.find([('user_id'. '=', '')]).fetchone()
			else return "Essa transacao e invalida"


		def save(self)
		transaction_id = self.model(self.get_request_parameters()).save().last_id()
		return "Done: Transaction {} created successfully".format(transaction_id)