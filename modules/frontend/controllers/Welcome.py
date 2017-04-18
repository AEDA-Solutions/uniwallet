from framework import Controller as std

class Welcome(std.Controller):

	def index(self):
		host = "http://{}:{}".format(self.request.env['SERVER_NAME'], self.request.env['SERVER_PORT'])
		html = self.get_html("index")
		html = html.replace("{assets-js}", "/frontend/static/js?target=assets/").replace("{assets-css}", "/frontend/static/css?target=assets/").replace("{assets-img}", "/frontend/static/img?target=assets/")
		return html



