from framework import Controller as std

class App(std.Controller):

	def prepare_static(self, html):
		return html.replace("{static}", "http://localhost:8008/")

	def cadastro(self):
		return self.prepare_static(self.get_html("cadastro"))

	def empresa(self):
		return self.prepare_static(self.get_html("cadastroEmpresa"))

	def inicial(self):
		return self.prepare_static(self.get_html("index"))

	def faleconosco(self):
		return self.prepare_static(self.get_html("faleconosco"))

	def usuario(self):
		return self.prepare_static(self.get_html("usuario"))

	def transaction(self):
		return self.prepare_static(self.get_html("CreateTransaction"))

	def gerenciamento(self):
		return self.prepare_static(self.get_html("AdminPanel"))

	def login(self):
		return self.prepare_static(self.get_html("login"))

	def sobre(self):
		return self.prepare_static(self.get_html("sobre"))

	def usuarioempresa(self):
		return self.prepare_static(self.get_html("usuarioEmpresa"))

	def referencias(self):
		return self.prepare_static(self.get_html("referencias").replace("{{tassila}}","Guilherme"))

	def empresa(self):
		return self.prepare_static(self.get_html("listaempresa"))

	def teste(self):
		return self.prepare_static(self.get_html("testedados"))

	def produtos(self):
		return self.prepare_static(self.get_html("listaprodutos"))

