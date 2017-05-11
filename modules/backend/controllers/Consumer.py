from framework import Controller as std

class Consumer(std.Controller):

	def set_accesses(self, user_id):
		self.model_class('User_AccessLevel')(database = self.get_db_connection(), data = {'user_id': user_id, 'accesslevel_id': 1}).check_save()
		self.model_class('User_AccessLevel')(database = self.get_db_connection(), data = {'user_id': user_id, 'accesslevel_id': 2}).check_save()
		
	def register(self):
		user_id = self.model_class('User')(database = self.get_db_connection(), data = {'email': self.get_input('email'), 'password': self.get_input('password')}).save().last_id()
		consumer_id = self.model(dict(list(self.get_request_parameters().items()) + list({"user_id": user_id}.items()))).save().last_id()
		self.set_accesses(user_id)
		return "Done: Consumer {} created with 'registered' and 'consumer' access level".format(user_id)