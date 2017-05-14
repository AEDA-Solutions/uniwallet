from framework import Controller as std

class Product(std.Controller):

	def register(self):
		product_id = self.model(self.get_request_parameters()).save().last_id()
		return "Done: Store {} created successfully".format(product_id)

	def fetch(self):
		return self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit')).fetch()


