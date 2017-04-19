from framework import Controller as std

class Pages(std.Controller):

	def cadastro(self):
		host = "http://{}:{}".format(self.request.env['SERVER_NAME'], self.request.env['SERVER_PORT'])
		html = self.get_html("TeladeCadastro")
		html = html.replace("{assets-js}", "/frontend/static/js?target=").replace("{assets-css}", "/frontend/static/css?target=").replace("{assets-img}", "/frontend/static/img?target=")
		return html

	def inicial(self):
		host = "http://{}:{}".format(self.request.env['SERVER_NAME'], self.request.env['SERVER_PORT'])
		html = self.get_html("index")
		html = html.replace("{assets-js}", "/frontend/static/js?target=").replace("{assets-css}", "/frontend/static/css?target=").replace("{assets-img}", "/frontend/static/img?target=")
		return html

	def arthur(self):
		return self.get_html("guilherme")