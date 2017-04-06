from framework import Controller as std

class Middleware(std.Controller):
	def forbid(self):
		self.response.code = 'Bad Request'

	def rules(self, rules, request):
		return self.validate(rules, request)

	def is_authorized(self, white_list):
		return True

	def check_fields(self, fields, request):
		response = []
		for key, value in fields.items():
			if 'required' in value and not key in request.body:
				response.append("{} field is required".format(key))
		if len(response):
			self.forbid()
		return response

	def validate(self, rules, request):
		if 'auth' in rules and not self.is_authorized(rules['auth']):
			self.forbid()
			return "Access denied"
		elif 'fields' in rules:
			return self.check_fields(rules['fields'], request)

