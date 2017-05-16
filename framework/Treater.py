from framework import Controller as std
from helpers import general, cpf, dictionary
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

	def check_authorization(self, user_id, credential_list):
		"""
		check_authorization(): It checks if the user is allowed to access the resource
		"""				
		if self.get_model('AccessLevel').user_has(user_id = user_id, credential_list = credential_list):
			self.request.user_id = user_id
		else:
			return self.forbid("You got access fuckin' denied")

	def rule_auth(self, auth):
		"""
		rule_auth(): It checks if the request is authorized to access the resource
		"""
		if len(auth):
			if self.request.authorization.exists:
				user_id = self.get_model('Session').get_user_id_vinculated(token = self.request.authorization.content, ip = self.request.client_ip)
				if user_id:
					return self.check_authorization(user_id, auth)
				else:
					return self.forbid("You got access fuckin' denied")
			else:
				return self.forbid("You got access fuckin' denied")

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

	"""""""""""""""""""""""""""""""""""""""
			FIELDS HANDLERS SECTION
	"""""""""""""""""""""""""""""""""""""""

	class FieldRule():
		"""
		class FieldRule: It represents the data passed to the field rule controllers
		"""
		def __init__(self, field_name, content, parameters, data_path):
			self.name = parameters[0] if len(parameters) > 0 else None
			self.field_name = field_name
			self.content = content
			self.data_path = data_path
			self.field_path = '.'.join(map(str, data_path + [field_name]))
			if len(parameters) > 0:
				del parameters[0]
			self.params = parameters

	def rule_fields(self, fields, data_path = []):
		"""
		rule_fields(): It checks the fields especifications
		"""
		response = self.check_forbidden_fields(list(field.replace('[]', '') for field in fields.keys()), data_path)
		if response:
			return response
		for field_name in fields.keys():
			if response:
				return response
			else:
				response = self.handle_field_rules(field_name, fields, data_path)
				if response:
					return response
			

	def handle_field_rules(self, field_name, fields, data_path):
		"""
		handle_fields(): It iterates the rules vinculated to the field and it calls the correspondent rule handler if necessary
		"""
		for field_rule in fields[field_name]:
			if isinstance(field_rule, dict):
				response = self.handle_subfields(field_rule, data_path + [field_name.replace('[]', '')])
			else:
				response = self.call_field_controller(field_rule, field_name.replace('[]', ''), data_path)
			if response:
				return response

	def check_listness(self, field_name, data_path):
		"""
		check_listness(): It checks if the field can be a list
		"""
		data = dictionary.access_nested_elem_from_list(self.get_request_parameters(), data_path)
		if '[]' not in field_name and field_name in data and isinstance(data[field_name], list):
			return self.forbid("{} cannot be a list".format('.'.join(map(str, data_path + [field_name]))))
		elif '[]' in field_name and field_name in data and not isinstance(data[field_name], list):
			return self.forbid("{} must be a list".format('.'.join(map(str, data_path + [field_name]))))

	def check_forbidden_fields(self, fields, data_path):
		"""
		check_forbidden_fields(): It checks if there is any input that does not correspond to any the defined fields
		"""
		data = dictionary.access_nested_elem_from_list(self.get_request_parameters(), data_path)
		if isinstance(data, dict):
			for input_name in data.keys():
				if input_name not in fields:
					return self.forbid("{} parameter is not acceptable".format("{}.{}".format('.'.join(data_path), input_name) if len(data_path) else input_name))

	def call_field_controller(self, field_rule, field_name, data_path):
		"""
		call_field_controller(): It tries to call an existent field controller
		"""
		field_method = getattr(self, "field_{}".format(field_rule.split(':')[0]), None)
		if callable(field_method):
			field_content = dictionary.access_nested_elem_from_list(self.get_request_parameters(), data_path + [field_name])
			if not isinstance(field_content, list):
				field_content = [field_content]
			if len(field_content) == 0:
				field_content = [""]
			response = field_method(self.FieldRule(field_name, field_content, field_rule.split(':'), data_path))
			if response:
				return response

	def handle_subfields(self, field_rule, data_path):
		"""
		field_field(): It handles fields that are fields themselves
		"""
		data = dictionary.access_nested_elem_from_list(self.get_request_parameters(), data_path)
		if isinstance(data, list):
			for pos, item in enumerate(data):
				response = self.rule_fields(field_rule, data_path + [pos])
				if response:
					return response
		else:
			response = self.rule_fields(field_rule, data_path)
			if response:
				return response

	def field_email(self, meta):
		"""
		field_email(): It checks if passed field is an email
		"""
		for pos, content in enumerate(meta.content):
			if not content or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", str(content)):
				return self.forbid("{} is not a valid email".format(meta.field_path, pos))
				

	def field_required(self, meta):
		"""
		field_required(): It checks if passed field exists or is not empty
		"""
		for pos, content in enumerate(meta.content):
			if content is None or len(str(content)) == 0:
				return self.forbid("{} parameter is required".format(meta.field_path, pos))

	def field_cpf(self, meta):
		"""
		field_cpf(): It checks if string is valid cpf
		"""
		for pos, content in enumerate(meta.content):
			if content is None or not cpf.is_cpf_valid(str(content)):
				return self.forbid("{} is an invalid cpf".format(meta.field_path, pos))

	def field_maxlength(self, meta):
		"""
		field_maxlength(): It checks max length for the content
		"""
		if len(meta.params) == 1:
			for pos, content in enumerate(meta.content):
				if content is not None and len(str(content)) > int(meta.params[0]):
					return self.forbid("Maximum length for {} is {}".format(meta.field_path, meta.params[0]))
		else:
			return self.forbid("Invalid '{}' rule sintax on Treater for {}".format(meta.name, meta.field_path))

	def field_minlength(self, meta):
		"""
		field_maxlength(): It checks max length for the content
		"""
		if len(meta.params) == 1:
			for pos, content in enumerate(meta.content):
				if content is not None and len(str(content)) < int(meta.params[0]):
					self.forbid()
					return "Minimum length for {} is {}".format(meta.field_path, meta.params[0])
		else:
			return self.forbid("Invalid '{}' rule sintax on Treater for {}".format(meta.name, meta.field_path))

	def field_exists(self, meta):
		"""
		field_exists(): It checks if field exists
		"""
		if len(meta.params) >= 1:
			for pos, content in enumerate(meta.content):
				model = self.get_model(self.__class__.__name__ if len(meta.params) == 1 else meta.params[1])
				connection = model.find([(meta.params[0], '=', content)])
				count = connection.cursor.rowcount
				connection.close()
				if count == 0:
					return self.forbid("{} does not exist as {}:{}".format(meta.field_path, meta.params[0], meta.params[1]))
		else:
			return self.forbid("Invalid '{}' rule sintax on Treater for {}".format(meta.name, meta.field_path))

	def field_unique(self, meta):
		"""
		field_unique(): It checks if field exists
		"""
		if len(meta.params) >= 1:
			data = dictionary.access_nested_elem_from_list(self.get_request_parameters(), meta.data_path)
			for pos, content in enumerate(meta.content):
				model = self.get_model(self.__class__.__name__ if len(meta.params) == 1 else meta.params[1])
				connection = model.find([(meta.params[0], '=', content)] + ([('id', '<>', data['id'])] if 'id' in data else []))
				count = connection.cursor.rowcount
				connection.close()
				if count != 0:
					return self.forbid("{} is already taken".format(meta.field_path))
		else:
			return self.forbid("Invalid '{}' rule sintax on Treater for {}".format(meta.name, meta.field_path))
	
	def field_integer(self, meta):
		"""
		field_integer(): It checks if field is an integer
		"""
		for pos, content in enumerate(meta.content):
			if content is None or not general.is_integer(str(content)):
				return self.forbid("{} is not an integer".format(meta.field_path, pos))
			else:
				if content is not None and 'unsigned' in meta.params and int(str(content)) < 0 or '-' in str(content):
					return self.forbid("{} is not an unsigned integer".format(meta.field_path, pos))

	def field_float(self, meta):
		"""
		field_float(): It checks if field is a float
		"""
		for pos, content in enumerate(meta.content):
			if content is None or not general.is_float(str(content)):
				return self.forbid("{} is not a float".format(meta.field_path, pos))

	def fetch(self):
		"""
		fetch(): It implements a default validator for the fetch request
		"""
		return self.rules({
				"fields": {
					"start": ["required", "integer:unsigned"],
					"limit": ["required", "integer:unsigned"],
					"_":	["optional"]
				},
				"method": "get",
				"auth": ["registered"]
			})

	def delete(self):
		"""
		destroy(): It implements a default validator for the destroy request
		"""
		return self.rules({
				"fields": {
					"data[]": ["required", {
						"id": ["required", "integer:unsigned"]
					}]
				},
				"method": "post",
				"auth": ["registered"]
			}) 