"""
Core

This structure is supposed to be inherited by all application entities.
It serves as a main provider for all the system.
"""

from framework.Response import Response
from framework.Database import Database
import importlib
from helpers import general, dictionary
import html
import os

class Core():
	def __init__(self, request):
		self.request = request

	def get_db_connection(self):
		"""
		get_db_connection(): It returns the current module database connection
		"""
		return Database(getattr(importlib.import_module("modules.{}.db.config".format(self.request.module)), "config")())

	def get_request_parameters(self):
		"""
		get_request_parameters(): It returns the request parameters in safe mode
		"""
		parameters = []
		for key, value in self.request.get_inputs_from_method().items():
			if isinstance(value, str):
				parameters.append(tuple([html.escape(key), html.escape(value)]))
			else:
				parameters.append(tuple([html.escape(key), value]))
		return dict(parameters)

	def get_raw_request_parameters(self):
		"""
		get_raw_request_parameters(): It returns the request parameters
		"""
		return self.request.get_inputs_from_method()

	def get_input(self, field):
		"""
		get_input(): It gets a request paramenter in safe mode
		"""
		if isinstance(self.request.get_input(field), str):
			return html.escape(self.request.get_input(field))
		else:
			return self.request.get_input(field)

	def get_raw_input(self, field):
		"""
		get_raw_input(): It gets a request paramenter
		"""
		return self.request.get_input(field)

	def get_file(self, file_path, mode = 'r'):
		"""
		get_file(): Get the file content
		"""
		pack = general.get_package_from_module(self.request.module, "modules")
		with open("{}/{}".format(os.path.dirname(pack.__file__), file_path), mode) as file:
			return file.read()

	def get_class(self, module_dir, class_name):
		"""
		get_class(): It returns a instance a of a correspondent model
		"""
		try:
			return getattr(importlib.import_module("modules.{}.{}.{}".format(self.request.module, module_dir, class_name)), class_name)
		except Exception as e:
			raise Exception("Error invoking class '{}': {}".format(class_name, str(e)))

	def make_where_conditions(self, dict, operator = '='):
		"""
		make_where_conditions(): It makes where conditions from a dict
		"""
		return dictionary.tuplefy(dict, operator)

	def controller(self, name = None):
		"""
		controller(): It returns a controller instance from the current module
		"""
		return self.get_class("controllers", self.__class__.__name__ if name is None else name)(request = self.request)

	def model(self, name = None, data = None):
		"""
		model(): It returns a model instance from the current module
		"""
		return self.get_class("models", self.__class__.__name__ if name is None else name)(request = self.request, data = data)

	def view(self, name = None):
		"""
		view(): It returns a view instance from the current module
		"""
		return self.get_class("views", self.__class__.__name__ if name is None else name)(request = self.request)



