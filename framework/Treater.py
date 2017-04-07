from framework import Controller as std

class Treater(std.Controller):
	def forbid(self):
		self.response.code = 'Bad Request'

	def rules(self, rules, request):
		return self.validate(rules, request)

	def is_authorized(self, white_list):
		return True

	def check_fields(self, fields, request):
		response = ""
		for key, value in fields.items():
			if 'required' in value and not key in request.body:
				response = "{} field is required".format(key)
				self.forbid()
				break			
		return response

	def validate(self, rules, request):
		if 'auth' in rules and not self.is_authorized(rules['auth']):
			self.forbid()
			return "Access denied"
		elif 'fields' in rules:
			return self.check_fields(rules['fields'], request)

