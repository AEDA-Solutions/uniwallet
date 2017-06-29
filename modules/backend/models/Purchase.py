from framework import Model as std

class Purchase(std.Model):
	attributes = ['transaction_id', 'company_id', 'consumer_id']

	def group_products_by_company(self, products):
		products_by_company = {}
		for item in products:
			company_id = self.model('Product').load(item["id"]).company_id 
			if company_id in products_by_company:
				products_by_company[company_id].append(item)
			else:
				products_by_company[company_id] = [item]
		return products_by_company

	def get_prices(self, products_by_company):
		prices_by_company = {}
		for company_id, products in products_by_company.items():
			prices_by_company[company_id] = 0
			for product in products:
				prices_by_company[company_id] += self.model('Product').get_price(product["id"], product["quantity"])
		return prices_by_company

	def get_sum_prices(self, prices_by_company):
		total_price = 0
		for company_id, price in prices_by_company.items():
			total_price += price
		return total_price

	def check_products_availability(self, products):
		for product in products:
			if not self.model('Product').check_product_available(product["id"], product["quantity"]):
				return False
		return True

	def prepare_products(self, products):
		if self.check_products_availability(products):
			return self.group_products_by_company(products)
		else:
			return None

	def perform(self, prices, products, user_id):

		#os.system("HTTP_PORT=3001 P2P_PORT=6001 npm start &")
		#os.system("HTTP_PORT=3002 P2P_PORT=6002 PEERS=ws://localhost:6001 npm start &")
		#os.system("curl -H \"Content-type:application/json\" --data '{\"data\" : \"Some data to the first block\"}' http://localhost:3001/mineBlock")

		consumer_id = self.model('Consumer').find(conditions = [('user_id', '=', user_id)]).fetchone()['id']
		wallet_from = self.model('Wallet').find(conditions = [('user_id', '=', user_id)]).fetchone()['id']
		for company_id, price in prices.items():
			wallet_to = self.model('Wallet').find(conditions = [('user_id', '=', self.model('Company').load(company_id).user_id)]).fetchone()['id']
			transaction_id = self.model(name = 'Transaction', data = {'wallet_from': wallet_from, 'wallet_to': wallet_to, 'value': price, 'operation': 'purchase'}).perform()
			if not transaction_id:
				return False
			purchase_id = self.model(data = {'transaction_id': transaction_id, 'consumer_id': consumer_id, 'company_id': company_id}).save().last_id()
			for product in products[company_id]:
				self.model("Product").load(product["id"]).decrement(product["quantity"])
				self.model(name = "Purchase_Product", data = {'purchase_id': purchase_id, 'product_id': product["id"], 'quantity': product["quantity"]}).save().close()

		return True


