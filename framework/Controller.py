from framework import Response as std
import importlib
from framework.helpers import general as helper
import app

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
			action_output = getattr(self, action_name)()
			return std.Response(code = self.response.code, body = action_output)
		else:
			return std.Response(code = 'Not Found', body = "Action '{}' unavailable".format(action_name))

	def model(self, data):
		"""
		get_model(): It returns a instance a of a correspondent model
		"""
		model_instance = None
		for model_name in helper.get_package_modules(app):
			if model_name == self.__class__.__name__:
				model_instance = getattr(importlib.import_module("app.{}".format(model_name)), model_name)(data)
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


