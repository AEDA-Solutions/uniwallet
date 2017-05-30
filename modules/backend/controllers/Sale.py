from framework import Controller as std

class Sale(std.Controller):

	def create(self):
		company_id = self.model(name = 'Session').get_user()['id']
		sale_id = self.model(data = {"company_id": company_id, "consumer_id": self.get_input("consumer_id")}).create().last_id()
		for product in self.get_input("products"):
			self.model(name = 'Sale_Product', data = {"sale_id": sale_id, "product_id": product['id'], "quantity": product['quantity']}).save().close()
		return "Espero que dê certo PORRW@!"

	def showall(self):
		lista = []
		sale_showall = self.model().find().fetch()
		#product_showall = self.model(name = 'Product').find().fetch()
		for sale in sale_showall:
			lista.append({'Sale':Sale,'Products':self.model(name = 'Product').find([('product_id','=',product['id'])]).fetch()})
		return (lista)
							

	def fetch(self):
		return self.model(name = 'Sale_Product').find(join = [('Product', 'product_id'), ('Company', 'Products.company_id'), ('Sale', 'sale_id'), ('Consumer', 'Sales.consumer_id')]).fetch()
		
	def total(self, sale_id):
		#retorna o valor total da SALE
		valor = 

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
		if wallet.check = ok #importar as funçoes
			transaction.save(destiny1, operation, value1)
			transaction.save(destiny2, operation, value2) 
			self.model(name = 'Wallet').find([ ('user_id', '=', sale_id)]).fetchone(fields = ['id'])