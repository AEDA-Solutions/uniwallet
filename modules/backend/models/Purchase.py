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

	def perform(self, products_by_company, wallet_from):
		for company_id, products in products_by_company.items():
			for product in products:
				return True
				pass #fui dormir aqui. Tava com muito sono



