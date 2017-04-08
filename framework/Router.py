from app import controllers
from app.controllers import treaters
from framework import Response as std
import importlib
from framework.helpers import general as helper
from framework.helpers import debugger as debugger
import sys, traceback

class Router():
	def __init__(self, request):
		self.request = request
		
	def route(self):
		"""
		route(): It chooses the appropriate controller
		"""
		if self.request.ok:
			try:
				return self.resolve()
			except:
				debugger.applog(traceback.format_exc())
				return std.Response(code = 'Internal Server Error', body = "I'm sorry Dave, I'm afraid I can't do that")
		else:
			return std.Response(code = 'Bad Request', body = "Invalid route")

	def resolve(self):
		"""
		resolve(): It call the specified controller
		"""
		treater = self.call_controller(treaters)
		if treater.code == 'OK' or treater.code == 'Not Found':
			return self.call_controller(controllers)
		else:
			return std.Response(code = treater.code, body = treater.body)

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
		controller = getattr(mod, controller_name)(self.request)
		return controller.action(self.request.action)

	
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