from framework import Controller as std

class App(std.Controller):

	def prepare_static(self, html):
		return html.replace("{static}", "http://localhost:8008/")

	def cadastro(self):
		return self.prepare_static(self.get_html("TeladeCadastro"))
		
	def empresa(self):
		return self.prepare_static(self.get_html("TeladeCadastroEmpresa"))

	def inicial(self):
		return self.prepare_static(self.get_html("index"))

	def faleconosco(self):
		return self.prepare_static(self.get_html("faleconosco"))

	def usuario(self):
		return self.prepare_static(self.get_html("TeladeUsuario"))

	def arthur(self):
		return self.get_html("guilherme")

	def transaction(self):
		return  self.prepare_static(self.get_html("CreateTransaction"))

	def motherfucker(self):
		return self.get_html("rafael")

	def gerenciamento(self):
		return self.prepare_static(self.get_html("AdminPanel"))

	def resumo(self):
		return self.prepare_static(self.get_html("sobre"))