from framework import Controller as std
from framework.Auth import Auth
import re

class Treater(std.Controller):

	def rules(self, rules):
		"""
		rules(): It receives the set rules
		"""
		return self.validate(rules)

	def validate(self, rules):
		"""
		validate(): It receives the rules and checks them
		"""
		rules_priority = ["private", "method", "auth", "fields"]
		for rule_name in rules_priority:
			if rule_name in rules.keys():
				rule_method = getattr(self, "rule_{}".format(rule_name), None)
				if callable(rule_method):
					response = rule_method(rules[rule_name])
					if response:
						return response

	def rule_auth(self, auth):
		"""
		rule_auth(): It checks if the request is authorized to access the resource
		"""
		#self.forbid()
		print(self.request.authorization)
		print(auth)

	def rule_method(self, method):
		"""
		rule_method(): It checks if the HTTP method is allowed
		"""
		if method.lower() != self.request.method.lower():
			self.forbid()
			return "{} HTTP method not allowed".format(self.request.method)

	def rule_private(self, is_private):
		"""
		rule_private(): It checks if the controller method is private
		"""
		if is_private:
			self.forbid()
			return "Access denied. This resource is private".format(self.request.action)

	def check_forbidden_fields(self, fields):
		"""
		check_forbidden_fields(): It checks if there is any input that does not correspond to any the defined fields
		"""
		for input_name in self.request.get_inputs_from_method().keys():
			if input_name not in fields.keys():
				self.forbid()
				return "{} parameter is not acceptable".format(input_name)

	def rule_fields(self, fields):
		"""
		rule_fields(): It checks the fields especifications
		"""
		response = self.check_forbidden_fields(fields)
		if response:
			return response
		for field_name in fields.keys():
			for field_rule in fields[field_name]:
				field_method = getattr(self, "field_{}".format(field_rule), None)
				if callable(field_method):
					response = field_method(field_name, self.request.get_input(field_name))
					if response:
						return response

	def field_email(self, field_name, field_content):
		"""
		field_email(): It checks if passed field is an email
		"""
		if not field_content or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", field_content):
			self.forbid()
			return "{} is not a valid email".format(field_name)

	def field_required(self, field_name, field_content):
		"""
		field_required(): It checks if passed field exists or is not empty
		"""
		if field_content is None or len(str(field_content)) == 0:
			self.forbid()
			return "{} parameter is required".format(field_name)

