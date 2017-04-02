class Response:
	def __init__(self):
		self.status = '200 OK'
		self.headers = {'Content-type':'text/html; charset=utf-8'}
		self.body = None
		self.ok = True

	def get_headers(self):
		return list(self.headers.items())

	def set_header(self, item, value):
		self.headers[item] = value

	def get_body(self):
		return self.body.encode("utf-8")

	def make_warning(self, msg):
		warning = Response()
		warning.ok = False
		warning.body = msg
		return warning
