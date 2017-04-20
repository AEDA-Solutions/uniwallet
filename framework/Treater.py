from framework import Controller as std
import re

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
			if 'email' in value:
				if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", self.request.get_inputs_from_method()[key]):
					response = "{} is not an valid email".format(key)
					self.forbid()
					break	

		return response

	def check_method(self, method):
		if method.lower() != self.request.method.lower():
			self.forbid()
			return "{} HTTP method not allowed".format(self.request.method)

	def check_privacy(self, is_private):
		if is_private:
			self.forbid()
			return "Access denied. This resource is private".format(self.request.action)

	def validate(self, rules):
		if 'private' in rules:
			response = self.check_privacy(rules['private'])
			if response:
				return response

		if 'auth' in rules and not self.is_authorized(rules['auth']):
			self.forbid()
			return "Access denied"

		if 'method' in rules:
			response = self.check_method(rules['method'])
			if response:
				return response

		if 'fields' in rules:
			response = self.check_fields(rules['fields'])
			if response:
				return response

