from framework import Controller as std

class Treater(std.Controller):
	def forbid(self):
		self.response.code = 'Bad Request'

	def rules(self, rules):
		return self.validate(rules)

	def is_authorized(self, white_list):
		return True

	def check_fields(self, fields):
		response = ""
		for key, value in fields.items():
			if 'required' in value:
				if not(key in self.request.get_inputs_from_method() and len(self.request.get_inputs_from_method()[key]) > 0):
					response = "{} field is required".format(key)
					self.forbid()
					break			
		return response

	def check_method(self, method):
		if method.lower() != self.request.method.lower():
			self.forbid()
			return "{} HTTP method not allowed".format(self.request.method)


	def validate(self, rules):
		if 'auth' in rules and not self.is_authorized(rules['auth']):
			self.forbid()
			return "Access denied"

		if 'method' in rules:
			response = self.check_method(rules['method'])
			if response and len(response):
				return response

		if 'fields' in rules:
			response = self.check_fields(rules['fields'])
			if response and len(response):
				return response

