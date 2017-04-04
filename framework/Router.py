from app import controllers
from framework import Response as std
import importlib
from framework.helpers import general as helper

class Router():
	def __init__(self, request, database):
		self.request = request
		self.database = database

	def route(self):
		"""
		route(): It delivers the request to the appropriate controller
		"""
		if self.request.ok:
			controller_name = self.parse_controller_name(self.request.controller)
			if controller_name:
				return self.get_controller_output(controller_name)
			else:
				return std.Response(ok = False, body = "Controller '{}' not found".format(self.request.controller))
		else:
			return std.Response(ok = False, body = "Invalid route")

	def parse_controller_name(self, cname):
		"""
		parse_controller_name(): It translates the passed controller name to the real file/class controller name
		"""
		controller_name = None
		for name in helper.get_package_modules(controllers):
			if cname.lower() == name.lower():
				controller_name = name
				break
		return controller_name

	def get_controller_output(self, controller_name):
		"""
		get_controller_output(): It makes a controller object and returns the action result
		"""
		mod = importlib.import_module("app.controllers.{}".format(controller_name))
		try:
			controller = getattr(mod, controller_name)(self.database)
		except Exception as err:
			return std.Response(ok = False, body = "Ops. Error calling controller: {}".format(str(err)))
		return self.run_action(controller)

	def run_action(self, controller):
		"""
		run_action(): It calls the specified action from the passed controller instance
		"""
		try:
			action_output = controller.action(self.request.action, self.request)
		except Exception as err:
			return std.Response(ok = False, body = "Ops. Error calling action: {}".format(str(err)))
		return action_output