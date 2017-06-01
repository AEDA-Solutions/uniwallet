from framework import Model as std

class Wallet(std.Model):
	attributes = ['balance', 'user_id']

	def do_something(self, value):
		return value + 1000

	def check(self, value):
		if value <= self.balance:
			return True
		else:
			return False

	def transfer(self, value, wallet_from, wallet_to):
		w_from = self.model().load(wallet_from)
		w_to = self.model().load(wallet_to)
		if w_from.check(value):
			w_from.balance -= value #It decrements the wallet balance with the value
			w_to.balance += value #It increments the wallet balance with the value
			#It saves the changes and closes de db connection
			w_from.save().close() 
			w_to.save().close()
			return True
		else:
			return False #It happens when value is not authorized to be transferred