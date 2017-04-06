from framework import Response as std
import importlib
from framework.helpers import general as helper
import app

class Controller:

	def __init__(self, database):
		self.response = std.Response()
		self.db = database

	def action(self, action_name, variables = None):
		"""
		action(): It tries to call a method called 'action_name' from the current Controller object. Then it returns the output of that method.
		If that method is not found, it returns a warning.
		"""
		if hasattr(self, action_name) and callable(getattr(self, action_name)):
			action_output = getattr(self, action_name)(variables)
			return std.Response(code = self.response.code, body = action_output)
		else:
			return std.Response(code = 'Not Found', body = "Action '{}' unavailable".format(action_name))

	def model(self):
		"""
		get_model(): It returns a instance a of a correspondent model
		"""
		model_instance = None
		for model_name in helper.get_package_modules(app):
			if model_name == self.__class__.__name__:
				model_instance = getattr(importlib.import_module("app.{}".format(model_name)), model_name)(self.db)
				break
		return model_instance


