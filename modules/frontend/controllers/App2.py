from framework import Controller as std

class App2(std.Controller):

	def prepare_static(self, html):
		return html.replace("{static}", "http://localhost:8008/")

	def cadastro(self):
		return self.prepare_static(self.get_html("cadastro_new"))

	def usuarioempresa(self):
		return self.prepare_static(self.get_html("usuarioEmpresa"))