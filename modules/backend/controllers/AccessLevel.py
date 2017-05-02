from framework import Controller as std

class AccessLevel(std.Controller):
	
	def register(self):
		return "Ok. {} rows affected".format(self.model(self.get_request_parameters()).save().count_rows())

	def empower(self):
		return "Ok. {} rows affected".format(self.model_class('User_AccessLevel')(data = self.get_request_parameters(), database = self.get_db_connection()).check_save())


