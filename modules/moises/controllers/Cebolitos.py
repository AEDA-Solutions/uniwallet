from framework import Controller as std

class Cebolitos(std.Controller):
		
	def arca(self):
		self.response_body_directly()
		return self.get_html("index")

	def salvar(self):
		self.model(self.get_request_parameters()).save().close()
		return "sucesso"

