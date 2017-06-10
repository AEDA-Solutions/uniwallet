from . import Controller as std

class Consumer(std.Controller):

	def set_accesses(self, user_id):
		self.model(name = 'User_AccessLevel', data = {'user_id': user_id, 'accesslevel_id': 1}).check_save()
		self.model(name = 'User_AccessLevel', data = {'user_id': user_id, 'accesslevel_id': 2}).check_save()

	def register(self):
		password = self.get_input('password') if self.get_input('password') is not None else '12345678'
		user_id = self.model(name = 'User', data = {'name': self.get_input('fullname'), 'email': self.get_input('email'), 'password': password}).save().last_id()
		consumer_id = self.model(data = dict(list(self.get_request_parameters().items()) + list({"user_id": user_id}.items()))).save().last_id()
		self.model(name = 'Wallet', data = {'user_id': user_id, 'balance': 100}).save().close()
		self.set_accesses(user_id)
		return "Done: Consumer {} created with 'registered' and 'consumer' access level".format(user_id)

	def update(self):
		consumer = self.model().load(self.get_input('id'))
		user = self.model(name = 'User').load(consumer.user_id)
		user.fill({'name': self.get_input('fullname'), 'email': self.get_input('email')}).save().close()
		rows = consumer.fill(self.get_request_parameters()).save().count_rows()
		return "Done: {} rows affected".format(rows)

	def fetch(self):
		fields_to_ignore = ['user_password', 'created_at', 'user_created_at', 'user_id', 'user_name']
		aliases = [('user_email', 'email'), ('user_name', 'user_name')]
		return self.model().find(join = [('User', 'user_id')], start_from = self.get_input('start'), limit = self.get_input('limit')).fetch(fields_to_ignore = ['user_password', 'created_at', 'user_created_at', 'user_id'])

	def fetchadmin(self):
		mask = self.metadata([('id', ':::hide'), ('user_id', ':::hide'), ('user_email', 'email:Email'), ('fullname', ':Nome'), ('cpf', ':CPF'), ('university_name', ':Universidade::noneditable'), ('university_id', ':Universidade:University')])
		return (self.model().find(join=[('User', 'user_id'), ('University', 'university_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))

	def extrato(self):
		user_id = self.model(name = 'Session').get_user()['id']
		wall_id = self.model("Wallet").find([('user_id', '=', user_id)]).fetchone("id")["id"]
		return self.model("Transaction").find(conditions = [("wallet_from", '=', wall_id)], join = [("Wallet", "wallet_from"), ("User", "Wallets.user_id")]).fetch()


