from framework.Core import Core
from framework.Response import Response
from helpers import general
import importlib
from modules.aliases import aliases as modules_aliases

class Application(Core):
	def __init__(self, request):
		super().__init__(request)
	
	def run(self):
		"""
		init(): It inits the application work
		"""
		return self.route()

	def route(self):
		"""
		route(): It chooses the appropriate controller
		"""
		if self.request.ok:
			return self.resolve()
		else:
			return Response(code = 'Not Found', body = 'Invalid route')

	def resolve(self):
		"""
		resolve(): It call the specified controller
		""" 
		if self.request.module in modules_aliases().keys():
			self.request.module = modules_aliases()[self.request.module]

		treater = self.call_controller(general.get_package_from_module("controllers.treaters", "modules.{}".format(self.request.module)))
		if treater.code == 'OK' or treater.code == 'Not Found':
			return self.call_controller(general.get_package_from_module("controllers", "modules.{}".format(self.request.module)))
		else:
			return Response(code = treater.code, body = treater.body)

	def call_controller(self, package):
		"""
		call_controller(): It tries to find the required controller
		"""
		controller_name = None
		if package:
			controller_name = self.translate_controller_name(package, self.request.controller)

		if controller_name:
			return self.instance_controller(package, controller_name)
		else:
			return self.controller('General').action('notfound')

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
		for name in general.get_package_modules(package):
			if raw_name.lower() == name.lower():
				controller_name = name
				break
		return controller_name