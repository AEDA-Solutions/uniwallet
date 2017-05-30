from framework import Controller as std
from framework.Session import get_user

class Wallet(std.Controller):

	def register(self):
		wallet_id = self.model(data = self.get_request_parameters()).save().last_id()
		return "Done: Wallet {} created successfully".format(wallet_id)

	def check(self, value):
		#confere se a carteira possui o valor desejado
		if value == self.model(name = 'Wallet').find([('user_id', '=', get_user())]).fetchone(fields = ['balance'])
			return "ok"
		else:
			return "fundo insuficiente"