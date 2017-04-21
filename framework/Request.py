from cgi import parse_qs, escape
from framework.helpers import translator as translator

class Request:
	def __init__(self, env):
		self.env = env
		self.urn = env['PATH_INFO']
		self.urn_list = self.urn.strip('/').split('/')
		self.ok = len(self.urn_list) >= 2
		self.module = '/'
		if self.ok:
			if len(self.urn_list) == 2:
				self.controller, self.action = self.urn_list[0].replace(".", ""), self.urn_list[1].replace(".", "")
			else:
				self.module, self.controller, self.action = self.urn_list[0].replace(".", ""), self.urn_list[1].replace(".", ""), self.urn_list[2].replace(".", "")
		self.body = self.translate_POST_content()
		self.parameters = self.get_GET()
		self.method = env['REQUEST_METHOD']

	def get_GET(self):
		"""
		get_GET(): It returns the variables passed through the url
		"""
		variables = parse_qs(self.env['QUERY_STRING'])
		treated_vars = {}
		for key in variables.keys():
			if isinstance(variables[key], list) and len(variables[key]) == 1:
				treated_vars[key] = variables[key][0]
			else:
				treated_vars[key.replace('[]', '')] = variables[key]
		return treated_vars

	def get_body_size(self):
		"""
		get_body_size(): It returns the size of the message received through the request
		"""
		try:
			request_body_size = int(self.env.get('CONTENT_LENGTH', 0))
		except (ValueError):
			request_body_size = 0
		return request_body_size

	def get_POST(self):
		"""
		get_POST(): This function reads the raw post content from the HTTP request
		"""
		request_body = self.env['wsgi.input'].read(self.get_body_size())
		return request_body.decode("utf-8")


	def translate_POST_content(self):
		"""
		translate_content(): It tries to convert the received message from JSON string to a dict
		"""
		POST_content = self.get_POST()
		if(POST_content):
			return translator.decode_JSON(POST_content)
		else:
			return {}

	def get_inputs_from_method(self):
		"""
		get_inputs_from_method(): It makes the inputs from the current method
		"""
		if self.method.lower() == 'get':
			return self.parameters
		else:
			return self.body

	def get_input(self, input_name):
		"""
		get_input(): It makes an input from the current method
		"""
		inputs = self.get_inputs_from_method()
		if input_name in inputs:
			return inputs[input_name]
		else:
			return None