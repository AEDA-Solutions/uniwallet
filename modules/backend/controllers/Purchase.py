from . import Controller as std
from pprint import pprint


class Purchase(std.Controller):

	def create(self):
		products =  self.model().prepare_products(self.get_request_parameters()["products"])
		if products != None:
			user_id = self.model(name = 'Session').get_user()['id']
			wallet_from = self.model('Wallet').find(conditions = [('user_id', '=', user_id)]).fetchone()['id']
			prices = self.model().get_prices(products)
			if self.model('Wallet').load(wallet_from).check(self.model().get_sum_prices(prices)):
				if self.model().perform(products, wallet_from):
					return "Everything in place"
				else:
					return self.forbid("Process interrupted", 'Unauthorized')
			else:
				return self.forbid("No funds", 'Unauthorized')
		else:
			return self.forbid("Products unavailable", 'Unauthorized')

	"""def create2 (self):
		consumer_id = self.model(name = 'Session').get_user()['id']
		total_price = 0
		i = 0
		products = []
		quantity = []
		products_by_company = {}
		values_to_transfer = {}

		for item in self.get_request_parameters()["products"]:
			company_id = self.model('Product').load(item["id"]).company_id 
			if company_id in products_by_company:
				products_by_company[company_id].append(item)
			else:
				products_by_company[company_id] = [item]

		for company_id, products in products_by_company.items():
			values_to_transfer[company_id] = 0

			for product in products:
				if not self.model('Product').check_product_available(product["id"], product["quantity"]):
					self.response.code = 'Unauthorized'
					return "Quantidade {} do Produto {} Indisponivel".format(product["id"], product["quantity"])
			
				values_to_transfer[company_id] += self.model('Product').get_price(product["id"], product["quantity"])
				total_price += values_to_transfer[company_id]



		wallet_from = self.model('Wallet').find(conditions = [('user_id', '=', self.model('Consumer').load(consumer_id).user_id)]).fetchone()['id']

		if self.model('Wallet').load(wallet_from).check(total_price):

			for company_id, value in values_to_transfer.items():
				wallet_to = self.model('Wallet').find(conditions = [('user_id', '=', self.model('Company').load(company_id).user_id)]).fetchone()['id']

				transaction_id = self.model(name = 'Transaction', data = {'wallet_from': wallet_from, 'wallet_to': wallet_to, 'value': total_price, 'operation': 'purchase'}).perform()
				if transaction_id is not None:

					purchase_id = self.model(data = {'transaction_id': transaction_id, 'consumer_id': consumer_id, 'company_id': company_id}).save().last_id()

					for product in products_by_company[company_id]:
						self.model(name = 'Purchase_Product', data = {'purchase_id': purchase_id, 'product_id': product["id"], 'quantity': product["quantity"]}).save().close()
					return "Compra Completa!"
				
				else:
					self.response.code = 'Unauthorized'
					return "That's odd, the transaction had to be interrupted. There's no money"
		else:
			self.response.code = 'Unauthorized'
			return "Purchase not authorized. Não há saldo suficiente";"""
			

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

