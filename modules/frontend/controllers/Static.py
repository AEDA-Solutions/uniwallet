from framework import Controller as std

class Static(std.Controller):

	def css(self):
		self.response_body_directly()
		self.response.set_headers([('content-type', 'text/css')])
		return self.get_file("static/{}".format(self.request.GET["target"][0]))

	def js(self):
		self.response_body_directly()
		self.response.set_headers([('content-type', 'text/javascript')])
		return self.get_file("static/{}".format(self.request.GET["target"][0]))

	def img(self):
		"""
		Finally it works, dude!!! It returns images placed on static/images
		"""
		self.response_body_directly()
		self.response.encode_before_transmission = False
		img = self.get_file("static/{}".format(self.request.GET["target"][0]), 'rb')
		self.response.set_headers([('content-type', 'image'), ('content-length', str(len(img)))])
		return img