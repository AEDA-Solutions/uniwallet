from framework import Controller as std

class Transaction(std.Controller):
	def __init__(self):
		super().__init__()

	def transfer(self, variables):
		return "Ok"