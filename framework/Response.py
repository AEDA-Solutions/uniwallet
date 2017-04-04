from framework.helpers import general as helper
from framework.helpers import translator as translator

class Response:
	def __init__(self, ok = True, body = None):
		self.status = '200 OK'
		self.headers = [('Content-type', 'text/html; charset=utf-8')]
		self.ok = ok
		self.body = body

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

	def prepare(self, response):
		return translator.encode_JSON({"ok": response.ok, "content": response.body}).encode("utf-8")
