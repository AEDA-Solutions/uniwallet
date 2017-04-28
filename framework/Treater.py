from framework import Controller as std
from framework.Auth import Auth
from framework.helpers import general as helper
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
			if input_name not in fields:
				self.forbid()
				return "{} parameter is not acceptable".format(input_name)

	def rule_fields(self, fields):
		"""
		rule_fields(): It checks the fields especifications
		"""
		response = self.check_forbidden_fields(helper.replace_on_list(list(fields.keys()), '[]', ''))
		if response:
			return response
		for field_name in fields.keys():
			response = self.check_listness(field_name)
			if response:
				return response
			for field_rule in fields[field_name]:
				response = self.call_field_controller(field_rule, field_name.replace('[]', ''))
				if response:
					return response
				
	def check_listness(self, field_name):
		"""
		check_listness(): It checks if the field can be a list
		"""
		if '[]' not in field_name and isinstance(self.request.get_input(field_name), list):
			self.forbid()
			return "{} cannot be a list".format(field_name)
		elif '[]' in field_name and not isinstance(self.request.get_input(field_name.replace('[]', '')), list):
			self.forbid()
			return "{} must be a list".format(field_name.replace('[]', ''))

	def call_field_controller(self, field_rule, field_name):
		"""
		call_field_controller(): It tries to call an existent field controller
		"""
		field_method = getattr(self, "field_{}".format(field_rule), None)
		if callable(field_method):
			field_content = self.request.get_input(field_name)
			if not isinstance(field_content, list):
				field_content = [field_content]
			if len(field_content) == 0:
				field_content = [""]
			response = field_method(field_name, field_content)
			if response:
				return response

	def field_email(self, field_name, field_content):
		"""
		field_email(): It checks if passed field is an email
		"""
		for pos, content in enumerate(field_content):
			if not content or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", content):
				self.forbid()
				return "{} is not a valid email".format(field_name, pos)

	def field_required(self, field_name, field_content):
		"""
		field_required(): It checks if passed field exists or is not empty
		"""
		for pos, content in enumerate(field_content):
			if content is None or len(str(content)) == 0:
				self.forbid()
				return "{} parameter is required".format(field_name, pos)

