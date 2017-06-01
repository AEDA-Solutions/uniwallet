from . import Controller as std

class Product(std.Controller):

	def register(self):
		product_id = self.model(data = self.get_request_parameters()).save().last_id()
		price = self.model(name = 'Product_Price', data = {'product_id': product_id, 'price': self.get_input('price')}).save().close()
		return "Done: Store {} created successfully".format(product_id)

	def fetch(self):
		return (self.model().find(join=[('Company', 'company_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch())

	def fetchadmin(self):
		mask = self.metadata([('id', 'id:::hide'), ('quantity', ':Quantidade'), ('name', ':Nome'), ('description', ':Descrição'), ('category', ':Categoria'), ('number', ':Número'), ('price', ':Preço'), ('company_id', ':Empresa:Company'), ('company_name', ':Empresa::noneditable')])
		return (self.model().find(join=[('Company', 'company_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))