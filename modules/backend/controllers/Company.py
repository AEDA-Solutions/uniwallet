from . import Controller as std

class Company(std.Controller):

	def set_accesses(self, user_id):
		self.model(name = 'User_AccessLevel', data = {'user_id': user_id, 'accesslevel_id': 1}).check_save()
		self.model(name = 'User_AccessLevel', data = {'user_id': user_id, 'accesslevel_id': 3}).check_save()
		
	def register(self):
		password = self.get_input('password') if self.get_input('password') is not None else '12345678'
		user_id = self.model(name = 'User', data = {'name': self.get_input('name'), 'email': self.get_input('email'), 'password': password}).save().last_id()
		company_id = self.model(data = dict(list(self.get_request_parameters().items()) + list({"user_id": user_id}.items()))).save().last_id()
		self.model(name = 'Wallet', data = {'user_id': user_id, 'balance': 100}).save().close()
		self.set_accesses(user_id)
		return "Done: Company {} created with 'registered' and 'company' access levels".format(user_id)
	
	def update(self):
		company = self.model().load(self.get_input('id'))
		user = self.model(name = 'User').load(company.user_id)
		user.fill({'name': self.get_input('name'), 'email': self.get_input('email')}).save().close()
		rows = company.fill(self.get_request_parameters()).save().count_rows()
		return "Done: {} rows affected".format(rows)

	def showall(self):
		lista = []
		company_showall = self.model().find().fetch()
		product_showall = self.model(name = 'Product').find().fetch()
		for company in company_showall:
			lista.append({'Company':company,'Products':self.model(name = 'Product').find([('company_id','=',company['id'])]).fetch()})
		return (lista)
							

	def fetch(self):
		fields_to_ignore = ['user_password', 'created_at', 'user_created_at', 'user_id', 'user_name']
		aliases = [('user_email', 'email'), ('user_name', 'user_name')]
		return self.model().find(join = [('User', 'user_id')], start_from = self.get_input('start'), limit = self.get_input('limit')).fetch(fields_to_ignore = fields_to_ignore, aliases = aliases)

	def select(self):
		return self.model().find().fetch(fields_mask = [('id', 'value'), ('name', 'content')])

	def fetchadmin(self):
		mask = self.metadata([('id', ':::hide'), ('user_id', ':::hide'), ('user_email', 'email:Email'), ('name', ':Nome'), ('cnpj', ':CNPJ')])
		return (self.model().find(join=[('User', 'user_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))
	
	def list(self):
		return self.model().find().fetch(fields=["name", "id"])