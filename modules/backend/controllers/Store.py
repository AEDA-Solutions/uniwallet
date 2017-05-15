from framework import Controller as std

class Store(std.Controller):

	def register(self):
		store_id = self.model(self.get_request_parameters()).save().last_id()
		return "Done: Store {} created successfully".format(store_id)

	def fetch(self):
		return self.model().find(join = [('Company', 'company_id'), ('User', 'Companies.user_id')], start_from = self.get_input('start'), limit = self.get_input('limit')).fetch(fields_to_ignore = ['company_created_at', 'company_id', 'user_password'])

	def append_product(self):
		last_id = self.get_model('Product_Store', self.get_request_parameters()).save().last_id()
		return "Done: Relation {} created successfully".format(last_id)

