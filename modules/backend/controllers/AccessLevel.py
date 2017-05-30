from . import Controller as std

class AccessLevel(std.Controller):
	
	def register(self):
		return "Ok. {} rows affected".format(self.model(data = self.get_request_parameters()).save().count_rows())

	def empower(self):
		return "Ok. {} rows affected".format(self.model(name = 'User_AccessLevel', data = self.get_request_parameters()).check_save())

	def select(self):
		return self.model().find().fetch(fields_mask = [('id', 'value'), ('name', 'content')])

	def fetch(self):
		return self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit')).fetch()

	def fetchadmin(self):
		mask = self.metadata([('id', ':::hide'), ('name', ':Nome'), ('description', ':Descrição')])
		return (self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))