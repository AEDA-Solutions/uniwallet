from framework.Controller import Controller

class General(Controller):

	def prepare_static(self, html):
		return html.replace("{static}", "http://localhost:8008/")
	
	def controllernotfound(self):
		return self.forbid(self.prepare_static(self.get_html("404")), 'Not Found')

	def actionnotfound(self):
		return self.forbid(self.prepare_static(self.get_html("404")), 'Not Found')


