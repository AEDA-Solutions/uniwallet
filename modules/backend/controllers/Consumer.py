from framework import Controller as std

class Consumer(std.Controller):

	def set_accesses(self, user_id):
		self.model(name = 'User_AccessLevel', data = {'user_id': user_id, 'accesslevel_id': 1}).check_save()
		self.model(name = 'User_AccessLevel', data = {'user_id': user_id, 'accesslevel_id': 2}).check_save()

	def register(self):
		user_id = self.model(name = 'User', data = {'name': self.get_input('fullname'), 'email': self.get_input('email'), 'password': self.get_input('password')}).save().last_id()
		consumer_id = self.model(data = dict(list(self.get_request_parameters().items()) + list({"user_id": user_id}.items()))).save().last_id()
		self.set_accesses(user_id)
		return "Done: Consumer {} created with 'registered' and 'consumer' access level".format(user_id)

	def update(self):
		consumer = self.model().load(self.get_input('id'))
		user = self.model(name = 'User').load(consumer.user_id)
		user.fill({'name': self.get_input('fullname'), 'email': self.get_input('email')}).save().close()
		rows = consumer.fill(self.get_request_parameters()).save().count_rows()
		return "Done: {} rows affected".format(rows)

	def fetch(self):
		return self.model().find(join = [('User', 'user_id')], start_from = self.get_input('start'), limit = self.get_input('limit')).fetch(fields_to_ignore = ['user_password', 'created_at', 'user_created_at', 'user_id'])

	def fetchadmin(self):
		mask = self.metadata([('id', 'id'), ('user_email', 'email:Email'), ('fullname', ':Nome'), ('cpf', ':CPF'), ('university', ':Universidade')])
		print(mask)
		return (self.model().find(join=[('User', 'user_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))