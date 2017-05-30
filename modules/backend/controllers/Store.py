from . import Controller as std

class Store(std.Controller):

	def register(self):
		store_id = self.model(data = self.get_request_parameters()).save().last_id()
		return "Done: Store {} created successfully".format(store_id)

	def fetch(self):
		return self.model().find(join = [('Company', 'company_id'), ('User', 'Companies.user_id')], start_from = self.get_input('start'), limit = self.get_input('limit')).fetch(fields_to_ignore = ['company_created_at', 'company_id', 'user_password'])

	def fetchadmin(self):
		mask = self.metadata([('id', ':::hide'), ('company_id', ':Empresa:Company'), ('company_name', ':Empresa::noneditable'), ('name', ':Nome')])
		return (self.model().find(join=[('Company', 'company_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))

	def append_product(self):
		last_id = self.model(name = 'Product_Store', data = self.get_request_parameters()).save().last_id()
		return "Done: Relation {} created successfully".format(last_id)

