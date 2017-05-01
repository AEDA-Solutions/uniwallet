from framework import Controller as std
from framework.Auth import Auth
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

	def get_id_field(self, fields):
		"""
		get_id_field(): It gets ids fields
		"""
		for field in fields.keys():
			if '*' in field:
				return {field.replace('*', ''): self.request.get_input(field.replace('*', ''))}

	def rule_fields(self, fields):
		"""
		rule_fields(): It checks the fields especifications
		"""
		response = self.check_forbidden_fields(list(field.replace('[]', '').replace('*', '') for field in fields.keys()))
		if response:
			return response
		for field_name in fields.keys():
			response = self.check_listness(field_name)
			if response:
				return response
			for field_rule in fields[field_name]:
				response = self.call_field_controller(field_rule, field_name.replace('[]', '').replace('*', ''), self.get_id_field(fields))
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

	class FieldRule():
		"""
		class FieldRule: It represents the data passed to the field rule controllers
		"""
		def __init__(self, field_name, content, identificator, parameters):
			self.name = parameters[0] if len(parameters) > 0 else None
			self.field_name = field_name
			self.content = content
			self.identificator = identificator
			if len(parameters) > 0:
				del parameters[0]
			self.params = parameters

	def call_field_controller(self, field_rule, field_name, identificator):
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
			response = field_method(self.FieldRule(field_name, field_content, identificator, field_rule.split(':')))
			if response:
				return response

	def field_email(self, meta):
		"""
		field_email(): It checks if passed field is an email
		"""
		for pos, content in enumerate(meta.content):
			if not content or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", str(content)):
				return self.forbid("{} is not a valid email".format(meta.field_name, pos))
				

	def field_required(self, meta):
		"""
		field_required(): It checks if passed field exists or is not empty
		"""
		for pos, content in enumerate(meta.content):
			if content is None or len(str(content)) == 0:
				return self.forbid("{} parameter is required".format(meta.field_name, pos))

	def field_cpf(self, meta):
		"""
		field_cpf(): It checks if string is valid cpf
		"""
		for pos, content in enumerate(meta.content):
			if content is None or not cpf.is_cpf_valid(str(content)):
				return self.forbid("{} is an invalid cpf".format(meta.field_name, pos))

	def field_maxlength(self, meta):
		"""
		field_maxlength(): It checks max length for the content
		"""
		if len(meta.params) == 1:
			for pos, content in enumerate(meta.content):
				if content is not None and len(str(content)) > int(meta.params[0]):
					return self.forbid("Maximum length for {} is {}".format(meta.field_name, meta.params[0]))
		else:
			return self.forbid("Invalid '{}' rule sintax on Treater for {}".format(meta.name, meta.field_name))

	def field_minlength(self, meta):
		"""
		field_maxlength(): It checks max length for the content
		"""
		if len(meta.params) == 1:
			for pos, content in enumerate(meta.content):
				if content is not None and len(str(content)) < int(meta.params[0]):
					self.forbid()
					return "Minimum length for {} is {}".format(meta.field_name, meta.params[0])
		else:
			return self.forbid("Invalid '{}' rule sintax on Treater for {}".format(meta.name, meta.field_name))

	def field_exists(self, meta):
		"""
		field_exists(): It checks if field exists
		"""
		if len(meta.params) == 2:
			for pos, content in enumerate(meta.content):
				model = self.model_class(meta.params[1])(self.get_db_connection())
				connection = model.find([{meta.params[0]: content}])
				count = connection.cursor.rowcount
				connection.close()
				if count == 0:
					return self.forbid("{} does not exist as {}:{}".format(meta.field_name, meta.params[0], meta.params[1]))
		else:
			return self.forbid("Invalid '{}' rule sintax on Treater for {}".format(meta.name, meta.field_name))

	def field_unique(self, meta):
		"""
		field_unique(): It checks if field exists
		"""
		if len(meta.params) == 1:
			for pos, content in enumerate(meta.content):
				model = self.model_class(self.__class__.__name__)(self.get_db_connection())
				connection = model.find([{meta.params[0]: content}], None if meta.identificator is None else [meta.identificator])
				count = connection.cursor.rowcount
				connection.close()
				if count != 0:
					return self.forbid("{} is already taken".format(meta.field_name))
		else:
			return self.forbid("Invalid '{}' rule sintax on Treater for {}".format(meta.name, meta.field_name))
	
	def field_integer(self, meta):
		'''
		Verifica apenas se a variavel é uma int ou não
		'''
		if isinstance(meta,int) is False:
			return self.forbid("{} is not a number".format(meta.field_name, pos))

