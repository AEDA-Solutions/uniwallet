from app import controllers
from app.controllers import middlewares
from framework import Response as std
import importlib
from framework.helpers import general as helper
from framework.helpers import debugger as debugger

class Router():
	def __init__(self, request, database):
		self.request = request
		self.database = database
		
	def route(self):
		"""
		route(): Route
		"""
		if self.request.ok:
			middleware = self.call_controller(middlewares)
			if middleware.code == 'OK' or middleware.code == 'Not Found':
				return self.call_controller(controllers)
			else:
				return std.Response(code = middleware.code, body = middleware.body)
		else:
			return std.Response(code = 'Bad Request', body = "Invalid route")

	def call_controller(self, package):
		"""
		call_controller(): It tries to find the required controller
		"""
		controller_name = self.translate_controller_name(package, self.request.controller)
		if controller_name:
			return self.instance_controller(package, controller_name)
		else:
			return std.Response(code = 'Not Found', body = "Controller '{}' not found".format(self.request.controller))

	def instance_controller(self, package, controller_name):
		"""
		instance_controller(): It makes a controller object and returns the action result
		"""
		mod = importlib.import_module(package.__name__ + ".{}".format(controller_name))
		try:
			controller = getattr(mod, controller_name)(self.database)
		except Exception as err:
			return std.Response(code = 'Internal Server Error', body = "Ops. Error calling controller: {}".format(str(err)))
		return self.execute_action(controller)

	
	def translate_controller_name(self, package, raw_name):
		"""
		translate_controller_name(): It translates the passed controller name to the real file/class controller name
		"""
		controller_name = None
		for name in helper.get_package_modules(package):
			if raw_name.lower() == name.lower():
				controller_name = name
				break
		return controller_name

	def execute_action(self, controller):
		"""
		execute_action(): It calls the specified action from the passed controller instance
		"""
		try:
			action_output = controller.action(self.request.action, self.request)
		except Exception as err:
			return std.Response(code = 'Internal Server Error', body = "Ops. Error calling action: {}".format(str(err)))
		return action_output