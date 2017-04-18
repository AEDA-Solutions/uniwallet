from framework import Response as std
import importlib
from framework.helpers import general as helper
import os

class Controller:

	def __init__(self, request):
		self.response = std.Response()
		self.request = request

	def action(self, action_name):
		"""
		action(): It tries to call a method called 'action_name' from the current Controller object. Then it returns the output of that method.
		If that method is not found, it returns a warning.
		"""
		if hasattr(self, action_name) and callable(getattr(self, action_name)):
			self.response.body = getattr(self, action_name)()
			return self.response
		else:
			return std.Response(code = 'Not Found', body = "Action '{}' unavailable".format(action_name))

	def get_db_config(self):
		"""
		get_db_config(): It returns the module db config details
		"""
		return getattr(importlib.import_module("modules.{}.db.config".format(self.request.module)), "config")()


	def model(self, data):
		"""
		get_model(): It returns a instance a of a correspondent model
		"""
		model_instance = None
		pack = helper.get_package_from_module(self.request.module, "modules")
		for model_name in helper.get_package_modules(pack):
			if model_name == self.__class__.__name__:
				model_instance = getattr(importlib.import_module("modules.{}.{}".format(self.request.module, model_name)), model_name)(self.get_db_config(), data)
				break
		if model_instance:
			return model_instance
		else:
			raise Exception("Error invoking model '{}'. This model is not created yet.".format(self.__class__.__name__))

	def get_request_parameters(self):
		"""
		get_request_parameters(): It returns the request body
		"""
		return self.request.body

	def get_html(self, html_file_name):
		"""
		get_html(): It reads and returns the content of some html file placed on modules/{current_module}/html
		"""
		self.response_body_directly()
		return self.get_file("html/{}.html".format(html_file_name))

	def get_file(self, file_path, mode = 'r'):
		"""
		get_file(): Get the file content
		"""
		pack = helper.get_package_from_module(self.request.module, "modules")
		with open("{}/{}".format(os.path.dirname(pack.__file__), file_path), mode) as file:
			return file.read()

	def response_body_directly(self):
		"""
		response_body_directly(): It sets response.raw as True
		"""
		self.response.raw = True


