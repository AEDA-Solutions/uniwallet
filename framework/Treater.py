from framework import Controller as std
from framework.Auth import Auth
from helpers import general
from helpers import cpf
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
			return self.forbid("{} HTTP method not allowed".format(self.request.method))

	def rule_private(self, is_private):
		"""
		rule_private(): It checks if the controller method is private
		"""
		if is_private:
			return self.forbid("Access denied. This resource is private".format(self.request.action))

	def check_forbidden_fields(self, fields):
		"""
		check_forbidden_fields(): It checks if there is any input that does not correspond to any the defined fields
		"""
		for input_name in self.request.get_inputs_from_method().keys():
			if input_name not in fields:
				return self.forbid("{} parameter is not acceptable".format(input_name))

	def rule_fields(self, fields):
		"""
		rule_fields(): It checks the fields especifications
		"""
		response = self.check_forbidden_fields(general.replace_on_list(list(fields.keys()), '[]', ''))
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
			return self.forbid("{} cannot be a list".format(field_name))
		elif '[]' in field_name and not isinstance(self.request.get_input(field_name.replace('[]', '')), list):
			return self.forbid("{} must be a list".format(field_name.replace('[]', '')))

	def call_field_controller(self, field_rule, field_name):
		"""
		call_field_controller(): It tries to call an existent field controller
		"""
		field_method = getattr(self, "field_{}".format(field_rule.split(':')[0]), None)
		if callable(field_method):
			field_content = self.request.get_input(field_name)
			if not isinstance(field_content, list):
				field_content = [field_content]
			if len(field_content) == 0:
				field_content = [""]
			response = field_method(field_name, field_content, field_rule.split(':'))
			if response:
				return response

	def field_email(self, name, content, parameter):
		"""
		field_email(): It checks if passed field is an email
		"""
		for pos, content in enumerate(content):
			if not content or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", str(content)):
				return self.forbid("{} is not a valid email".format(name, pos))
				

	def field_required(self, name, content, meta):
		"""
		field_required(): It checks if passed field exists or is not empty
		"""
		for pos, content in enumerate(content):
			if content is None or len(str(content)) == 0:
				return self.forbid("{} parameter is required".format(name, pos))

	def field_cpf(self, name, content, meta):
		"""
		field_cpf(): It checks if string is valid cpf
		"""
		for pos, content in enumerate(content):
			if content is None or not cpf.is_cpf_valid(str(content)):
				return self.forbid("{} is an invalid cpf".format(name, pos))

	def field_maxlength(self, name, content, meta):
		"""
		field_maxlength(): It checks max length for the content
		"""
		if len(meta) == 2:
			for pos, content in enumerate(content):
				if content is not None and len(str(content)) > int(meta[1]):
					return self.forbid("Maximum length for {} is {}".format(name, meta[1]))
		else:
			return self.forbid("Invalid '{}' rule sintax on Treater for {}".format(meta[0], name))

	def field_minlength(self, name, content, meta):
		"""
		field_maxlength(): It checks max length for the content
		"""
		if len(meta) == 2:
			for pos, content in enumerate(content):
				if content is not None and len(str(content)) < int(meta[1]):
					self.forbid()
					return "Minimum length for {} is {}".format(name, meta[1])
		else:
			return self.forbid("Invalid '{}' rule sintax on Treater for {}".format(meta[0], name))

	def field_exists(self, name, content, meta):
		"""
		field_exists(): It checks if field exists
		"""
		if len(meta) == 3:
			for pos, content in enumerate(content):
				model = self.model_class(meta[2])(self.get_db_connection())
				connection = model.find({meta[1]: content})
				count = connection.cursor.rowcount
				connection.close()
				if count == 0:
					return self.forbid("{} does not exist as {}:{}".format(name, meta[1], meta[2]))
		else:
			return self.forbid("Invalid '{}' rule sintax on Treater for {}".format(meta[0], name))

	def field_unique(self, name, content, meta):
		"""
		field_unique(): It checks if field exists
		"""
		for pos, content in enumerate(content):
			model = self.model_class(self.__class__.__name__)(self.get_db_connection())
			connection = model.find({name: content})
			count = connection.cursor.rowcount
			connection.close()
			if count != 0:
				return self.forbid("{} is already taken".format(name))

