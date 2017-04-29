from framework.Response import Response
from framework.Database import Database
from helpers import general as helper
import importlib
import os

class Controller:

	def __init__(self, request):
		self.response = Response()
		self.request = request

	def get_module_nome(self):
		"""
		get_module_name(): It gets the module name where controller is located into
		"""
		pass

	def action(self, action_name):
		"""
		action(): It tries to call a method called 'action_name' from the current Controller object. Then it returns the output of that method.
		If that method is not found, it returns a warning.
		"""
		if hasattr(self, action_name) and callable(getattr(self, action_name)):
			self.response.body = getattr(self, action_name)()
			return self.response
		else:
			return Response(code = 'Not Found', body = "Action '{}' unavailable".format(action_name))

	def get_db_connection(self):
		"""
		get_db_connection(): It returns the database connection
		"""
		return Database(getattr(importlib.import_module("modules.{}.db.config".format(self.request.module)), "config")())


	def model(self, data = None):
		"""
		get_model(): It returns a instance a of a correspondent model
		"""
		pack = helper.get_package_from_module(self.request.module, "modules")
		model_name = None
		for model in helper.get_package_modules(pack):
			if model == self.__class__.__name__:
				model_name = model
				model_class = getattr(importlib.import_module("modules.{}.{}".format(self.request.module, model)), model)
				break
		return self.model_class(model_name)(self.get_db_connection(), data)

	def model_class(self, model_name):
		"""
		model_class(): It returns a instance a of a correspondent model
		"""
		try:
			return getattr(importlib.import_module("modules.{}.{}".format(self.request.module, model_name)), model_name)
		except:
			raise Exception("Error invoking model '{}'. This model does not exist.".format(model_name))

	def get_request_parameters(self):
		"""
		get_request_parameters(): It returns the request parameters
		"""
		return self.request.get_inputs_from_method()

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

	def forbid(self, message = None):
		"""
		forbid(): It sets the code as 400
		"""
		self.response.code = 'Bad Request'
		if message:
			return message 


