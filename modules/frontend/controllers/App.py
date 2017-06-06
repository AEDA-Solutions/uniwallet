from framework import Controller as std

class App(std.Controller):

	def prepare_static(self, html):
		return html.replace("{static}", "http://localhost:8008/")

	def cadastro(self):
		return self.prepare_static(self.get_html("cadastro"))

	def cadastroempresa(self):
		return self.prepare_static(self.get_html("cadastroEmpresa"))

	def inicial(self):
		return self.prepare_static(self.get_html("index"))

	def faleconosco(self):
		return self.prepare_static(self.get_html("faleconosco"))

	def usuario(self):
		return self.prepare_static(self.get_html("usuario"))

	def usuarioempresa(self):
		return self.prepare_static(self.get_html("usuarioEmpresa"))

	def transaction(self):
		return self.prepare_static(self.get_html("CreateTransaction"))

	def gerenciamento(self):
		return self.prepare_static(self.get_html("AdminPanel"))

	def login(self):
		return self.prepare_static(self.get_html("login"))

	def sobre(self):
		return self.prepare_static(self.get_html("sobre"))

	def listaempresas(self):
		return self.prepare_static(self.get_html("listaempresas"))

	def listaprodutos(self):
		return self.prepare_static(self.get_html("listaprodutos"))

	def editausuario(self):
		return self.prepare_static(self.get_html("editausuario"))

	def perfiledit(self):
		return self.prepare_static(self.get_html("perfiledit"))

	def teste(self):
		return self.prepare_static(self.get_html("Teste"))

	def tteste(self):
		return self.prepare_static(self.get_html("tteste"))

	def loja(self):
		return self.prepare_static(self.get_html("lojavirtual"))

		