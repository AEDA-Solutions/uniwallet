from framework.helpers import general as helper

class Response:
	def __init__(self):
		self.status = '200 OK'
		self.headers = [('Content-type', 'text/html; charset=utf-8')]
		self.body = None
		self.ok = True

	def set_headers(self, headers):
		"""
		set_headers(): It defines directly the response headers
		"""
		self.headers = headers

	def append_header(self, header):
		"""
		append_header(): This function gets a header and append it to the headers list. 
		If the header is already defined, the header content is replaced by the new value.
		"""
		self.headers = helper.fit_pair_to_list(self.headers, header)

	def get_body(self):
		"""
		get_body(): It gets the body content and prepare it to be transmitted through the web.
		"""
		return self.body.encode("utf-8")

	def make_warning(self, msg):
		"""
		make_warning(): It returns a default warning message.
		"""
		warning = Response()
		warning.ok = False
		warning.body = msg
		return warning
