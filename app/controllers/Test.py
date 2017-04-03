from framework import Controller as std

class Test(std.Controller):
	def __init__(self):
		super().__init__()

	def coisa(self, variables):
		return "Oi"