from framework import Controller as std

class Product(std.Controller):

	def register(self):
		product_id = self.model(data = self.get_request_parameters()).save().last_id()
		price = self.model(name = 'Product_Price', data = {'product_id': product_id, 'price': self.get_input('price')}).save().close()
		return "Done: Store {} created successfully".format(product_id)

	def fetch(self):
		mask = self.metadata([('number', 'Número'), ('price', 'Preço'), ('company_id', 'Empresa:company_id'), ('company_name', 'Empresa::noneditable')])
		return (self.model().find(join=[('Company', 'company_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))


