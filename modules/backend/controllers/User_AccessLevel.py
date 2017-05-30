from . import Controller as std

class User_AccessLevel(std.Controller):
	
	def register(self):
		return "Ok. {} rows affected".format(self.model(data = self.get_request_parameters()).save().count_rows())

	def fetch(self):
		return self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit')).fetch()

	def fetchadmin(self):
		mask = self.metadata([('id', ':::hide'), ('user_name', ':Usuário::noneditable'), ('accesslevel_name', ':Nível de acesso::noneditable'), ('user_id', ':Usuário:User'), ('accesslevel_id', ':Nível de acesso:AccessLevel')])
		return (self.model().find(join = [('User', 'user_id'), ('AccessLevel', 'accesslevel_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))
