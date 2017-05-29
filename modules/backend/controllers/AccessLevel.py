from framework import Controller as std

class AccessLevel(std.Controller):
	
	def register(self):
		return "Ok. {} rows affected".format(self.model(data = self.get_request_parameters()).save().count_rows())

	def empower(self):
		return "Ok. {} rows affected".format(self.model(name = 'User_AccessLevel', data = self.get_request_parameters()).check_save())

	def fetch(self):
		return self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit')).fetch()

