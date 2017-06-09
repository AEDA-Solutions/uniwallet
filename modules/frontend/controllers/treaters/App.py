from framework import Treater as std

class App(std.Treater):

	def prepare_static(self):
		return self.rules({
				"private": True
			})

	def usuarioempresa(self):
		return self.rules({
				"auth": []
			})