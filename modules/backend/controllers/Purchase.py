from . import Controller as std

class Purchase(std.Controller):

	def create(self):
		consumer_id = self.model(name = 'Session').get_user()['id']
		total_price = 0
		for item in self.get_request_parameters()["products"]:
			if not self.model('Product').check_product_available(item["id"], item["quantity"]):
				return "Proibido"
			total_price = total_price + self.model('Product').get_price(item["id"], item["quantity"])

		company_id = self.get_input('company_id')

		wallet_from = self.model('Wallet').find(conditions = [('user_id', '=', self.model('Consumer').load(consumer_id).user_id)]).fetchone()['id']
		wallet_to = self.model('Wallet').find(conditions = [('user_id', '=', self.model('Company').load(company_id).user_id)]).fetchone()['id']

		transaction_id = self.model(name = 'Transaction', data = {'wallet_from': wallet_from, 'wallet_to': wallet_to, 'value': total_price, 'operation': 'purchase'}).perform()
		if transaction_id is not None:
			self.model(data = {'transaction_id': transaction_id, 'consumer_id': consumer_id, 'company_id': company_id}).save().close()
			return "Purchase completed"
		else:
			return "Purchase not authorized"

	def showall(self):
		lista = []
		sale_showall = self.model().find().fetch()
		#product_showall = self.model(name = 'Product').find().fetch()
		for sale in sale_showall:
			lista.append({'Sale':Sale,'Products':self.model(name = 'Product').find([('product_id','=',product['id'])]).fetch()})
		return (lista)
							

	def fetch(self):
		return self.model(name = 'Sale_Product').find(join = [('Product', 'product_id'), ('Company', 'Products.company_id'), ('Sale', 'sale_id'), ('Consumer', 'Sales.consumer_id')]).fetch()

	def fetchadmin(self):
		mask = self.metadata([('id', ':::hide'), ('consumer_fullname', ':Comprador::noneditable'), ('company_name', ':Empresa::noneditable'), ('transaction_value', ':Valor::noneditable')])
		return (self.model().find(join=[('Transaction', 'transaction_id'), ('Consumer', 'consumer_id'), ('Company', 'company_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))

	def total(self, sale_id):
		#retorna o valor total da SALE
		valor = None

		self.model(name = 'Sale').find([ ('id', '=', sale_id)]).fetchone(fields = ['products'])
		#somatorio(ids * quantity)
		return valor
	def company_sale(self, sale_id):
		# retorna o user_id do vendedor
		com_id = self.model(name = 'Sale').find([ ('id', '=', sale_id)]).fetchone(fields = ['company_id'])
		us_id = self.model(name = 'Company').find([ ('id', '=', com_id)]).fetchone(fields = ['user_id'])
		return us_id
	
	def consumer_sale(self, sale_id):
		#retorna o user_id do consumidor
		con_id = self.model(name = 'Sale').find([ ('id', '=', sale_id)]).fetchone(fields = ['consumer_id'])
		us_id = self.model(name = 'Consumer').find([ ('id', '=', con_id)]).fetchone(fields = ['user_id'])
		return us_id
	


	def do_sale(self, sale_id):
		# cria 2 transaçoes: para a compania com valor positivo, e para o consumidor com valor negativo
		# confere se a carteira do consumir tem dinheiro
		destiny1 = self.model(name = 'Wallet').find([ ('user_id', '=', company_sale(sale_id))]).fetchone(fields = ['id'])
		destiny2 = self.model(name = 'Wallet').find([ ('user_id', '=', consumer_sale(sale_id))]).fetchone(fields = ['id'])
		operation = 'sale'
		value1 = total(sale_id)
		value2 = -total(sale_id)
		if wallet.check == ok: #importar as funçoes
			transaction.save(destiny1, operation, value1)
			transaction.save(destiny2, operation, value2) 
			self.model(name = 'Wallet').find([ ('user_id', '=', sale_id)]).fetchone(fields = ['id'])