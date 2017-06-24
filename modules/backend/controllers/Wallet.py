from . import Controller as std

class Wallet(std.Controller):

	def register(self):
		wallet_id = self.model(data = self.get_request_parameters()).save().last_id()
		return "Done: Wallet {} created successfully".format(wallet_id)

	def update(self):
		wallet = self.model().load(self.get_input('id'))
		wallet.balance = self.get_input('balance')
		return "Done: {} rows affected".format(wallet.save().count_rows())

	def fetchadmin(self):
		mask = self.metadata([('id', ':::hide'), ('user_name', ':Nome::noneditable'), ('balance', ':Saldo ($uni)')])
		return (self.model().find(join=[('User', 'user_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))

	def balance(self):
		user_id = self.model(name = 'Session').get_user()['id']
		balance = self.model().find([("user_id", "=", user_id)]).fetchone()["balance"]
		return balance

	def user(self):
		return self.get_input("wallet_idw")
		"""user_id = self.model().load(self.get_request_parameters()['wallet_id'])
		i_d = self.model(data = 
		user = self.model("User").find([("id", "=", i_d)]).fetchone()["name"]
		return user"""


