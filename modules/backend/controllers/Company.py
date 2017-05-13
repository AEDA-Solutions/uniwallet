from framework import Controller as std

class Company(std.Controller):

	def set_accesses(self, user_id):
		self.model_class('User_AccessLevel')(database = self.get_db_connection(), data = {'user_id': user_id, 'accesslevel_id': 1}).check_save()
		self.model_class('User_AccessLevel')(database = self.get_db_connection(), data = {'user_id': user_id, 'accesslevel_id': 3}).check_save()
		
	def register(self):
		user_id = self.model_class('User')(database = self.get_db_connection(), data = {'email': self.get_input('email'), 'password': self.get_input('password')}).save().last_id()
		consumer_id = self.model(dict(list(self.get_request_parameters().items()) + list({"user_id": user_id}.items()))).save().last_id()
		self.set_accesses(user_id)
		return "Done: Company {} created with 'registered' and 'company' access levels".format(user_id)

	def fetch(self):
		return self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit')).fetch(fields_to_ignore = ['password', 'created_at'])


