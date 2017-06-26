from framework import Controller as std

class App(std.Controller):

	def prepare_static(self, html):
		return html.replace("{static}", "http://localhost:8008/")

	def cadastro(self):
		return self.prepare_static(self.get_html("cadastro2"))

	def cadastroempresa(self):
		return self.prepare_static(self.get_html("empresario"))

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

	def listaprodutos(self):
		return self.prepare_static(self.get_html("listaprodutos"))

	def editausuario(self):
		return self.prepare_static(self.get_html("editausuario"))

	def perfiledit(self):
		return self.prepare_static(self.get_html("perfiledit"))

	def loja(self):
		return self.prepare_static(self.get_html("lojavirtual"))

	def rafa(self):
		return self.prepare_static(self.get_html("ajudarafa"))

	def lojaempresa(self):
		return self.prepare_static(self.get_html("lojaempresa"))

	def teste1(self):
		return self.prepare_static(self.get_html("teste1"))
	
	def lojaempresa1(self):
		return self.prepare_static(self.get_html("lojaempresa1"))
		