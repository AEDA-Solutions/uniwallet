from . import Controller as std
import os


class Purchase(std.Controller):

	def create(self):
		products =  self.model().prepare_products(self.get_request_parameters()["products"])
		if products != None:
			user_id = self.model(name = 'Session').get_user()['id']
			wallet_from = self.model('Wallet').find(conditions = [('user_id', '=', user_id)]).fetchone()['id']
			prices = self.model().get_prices(products)
			if self.model('Wallet').load(wallet_from).check(self.model().get_sum_prices(prices)):
				if self.model().perform(prices, products, user_id):
					return "Everything in place"
				else:
					return self.forbid("Process interrupted", 'Unauthorized')
			else:
				return self.forbid("No funds", 'Unauthorized')
		else:
			return self.forbid("Products unavailable", 'Unauthorized')

	def showall(self):
		lista = []
		purchase_showall = self.model().find().fetch()
		transaction_showall = self.model(name = 'Transaction').find().fetch()
		for purchase in purchase_showall:
			lista.append({'Purchase':purchase,'Transaction':self.model(name = 'Transaction').find([('user_id','=',user['id'])]).fetch()})
		return (lista)
							

	def fetch(self):
		return self.model(name = 'Sale_Product').find(join = [('Product', 'product_id'), ('Company', 'Products.company_id'), ('Sale', 'sale_id'), ('Consumer', 'Sales.consumer_id')]).fetch()

	def fetchadmin(self):
		mask = self.metadata([('id', ':::hide'), ('consumer_fullname', ':Comprador::noneditable'), ('company_name', ':Empresa::noneditable'), ('transaction_value', ':Valor::noneditable')])
		return (self.model().find(join=[('Transaction', 'transaction_id'), ('Consumer', 'consumer_id'), ('Company', 'company_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))

