from framework import Controller as std

class User(std.Controller):
	
	def register(self):
		user_id = self.model(self.get_request_parameters()).save().last_id()
		self.model_class('User_AccessLevel')(database = self.get_db_connection(), data = {'user_id': user_id, 'accesslevel_id': 1}).check_save()
		return "Done: User {} created with 'registered' access level".format(user_id)

	def update(self):
		return "Done: {} rows affected".format(self.model(self.get_request_parameters()).save().count_rows())

	def delete(self):
		return "Done: {} rows affected".format(self.model().destroy(list({'id': item} for item in self.get_request_parameters()['ids'])).count_rows())

	def fetch(self):
		return self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit')).fetch(fields_to_ignore = ['password'])
