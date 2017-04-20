from framework import Controller as std

class Pages(std.Controller):

	def prepare_static(self, html):
		return html.replace("{static}", "http://localhost:8008/")

	def cadastro(self):
		return self.prepare_static(self.get_html("TeladeCadastro"))

	def inicial(self):
		return self.prepare_static(self.get_html("index"))

	def arthur(self):
		return self.get_html("guilherme")