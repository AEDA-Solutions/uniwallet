from framework import Controller as std

class Sale(std.Controller):

	def create(self):
		company_id = self.get_model('Session').get_user()['id']
		sale_id = self.model({"company_id": company_id, "consumer_id": self.get_input("consumer_id")}).create().last_id()
		for product in self.get_input("products"):
			self.get_model(name = 'Sale_Product', data = {"sale_id": sale_id, "product_id": product['id'], "quantity": product['quantity']}).save().close()
		return "Espero que dê certo PORRW@!"

	def fetch(self):
		return self.get_model('Sale_Product').find(join = [('Product', 'product_id'), ('Company', 'Products.company_id'), ('Sale', 'sale_id'), ('Consumer', 'Sales.consumer_id')]).fetch(fields_mask = [('consumer_fullname', 'mané quue comprou'), ('company_name', 'Capitalista opressor patriarcal'), ('product_name', 'Fruto do capitalismo')])
		
