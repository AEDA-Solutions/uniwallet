from framework.helpers import general as helper

class Response:
	def __init__(self):
		self.status = '200 OK'
		self.headers = [('Content-type', 'text/html; charset=utf-8')]
		self.body = None
		self.ok = True

	def set_headers(self, headers):
		self.headers = headers

	def append_header(self, header):
		self.headers = helper.fit_pair_to_list(self.headers, header)

	def get_body(self):
		return self.body.encode("utf-8")

	def make_warning(self, msg):
		warning = Response()
		warning.ok = False
		warning.body = msg
		return warning
