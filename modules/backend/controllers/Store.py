from framework import Controller as std

class Store(std.Controller):

	def register(self):
		store_id = self.model(self.get_request_parameters()).save().last_id()
		return "Done: Store {} created successfully".format(store_id)

	def fetch(self):
		return self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit')).fetch()

	def append_product(self):
		last_id = self.model_class('Product_Store')(database = self.get_db_connection(), data = self.get_request_parameters()).save().last_id()
		return "Done: Relation {} created successfully".format(last_id)

