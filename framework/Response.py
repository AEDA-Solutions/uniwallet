from framework.helpers import general as helper
from framework.helpers import translator as translator

class Response:
	def __init__(self, code = 'OK', body = None):
		self.status = '200 OK'
		self.headers = [('Content-type', 'text/html; charset=utf-8')]
		self.code = code
		self.body = body

	def translate_code(self, code):
		"""
		translate_code(): Check out https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
		"""
		codes = {
		'OK': 200,
		'Bad Request': 400,
		'Forbidden': 403,
		'Not Found': 404,
		'Internal Server Error': 500
		}
		return codes[code]

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
		"""
		prepare(): This function makes a transmittable response
		"""
		return translator.encode_JSON({"code": self.translate_code(response.code), "content": response.body}).encode("utf-8")
