from framework import Controller as std

class Company(std.Controller):

	def set_accesses(self, user_id):
		self.get_model('User_AccessLevel', {'user_id': user_id, 'accesslevel_id': 1}).check_save()
		self.get_model('User_AccessLevel', {'user_id': user_id, 'accesslevel_id': 3}).check_save()
		
	def register(self):
		user_id = self.get_model('User', {'name': self.get_input('name'), 'email': self.get_input('email'), 'password': self.get_input('password')}).save().last_id()
		consumer_id = self.model(dict(list(self.get_request_parameters().items()) + list({"user_id": user_id}.items()))).save().last_id()
		self.set_accesses(user_id)
		return "Done: Company {} created with 'registered' and 'company' access levels".format(user_id)
	
	def showall(self):
		lista = []
		company_showall = self.model().find().fetch()
		product_showall = self.get_model('Product').find().fetch()
		for company in company_showall:
			lista.append({'Company':company,'Products':self.get_model('Product').find([('company_id','=',company['id'])]).fetch()})
		return (lista)
							

	def fetch(self):
		return self.model().find(join = [('User', 'user_id')], start_from = self.get_input('start'), limit = self.get_input('limit')).fetch(fields_to_ignore = ['user_password', 'created_at', 'user_created_at'])


