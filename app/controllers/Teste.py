from framework import Controller as default

class Teste(default.Controller):
	def __init__(self):
		super().__init__()

	def coisa(self):
		return "Oi"