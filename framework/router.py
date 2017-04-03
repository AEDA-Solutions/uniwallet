from app import controllers
from framework import Response as default
import importlib
from framework.helpers import general as helper

def route(request):
	"""
	route(): It delivers the request to the appropriate controller
	"""
	if request.ok:
		controller_name = parse_controller_name(request.controller)
		if controller_name:
			return call_controller(controller_name, request)
		else:
			return default.Response().make_warning("Controller {} not found".format(request.controller))
	else:
		return default.Response().make_warning("Incorrect request")

def call_controller(controller_name, request):
	"""
	call_controller(): It instances a controller of type 'controller_name' and returns the action output
	"""
	mod = importlib.import_module("app.controllers.{}".format(controller_name))
	ctrl = getattr(mod, controller_name)()
	try:
		action_output = ctrl.action(request.action, request)
	except Exception as err:
		action_output = default.Response().make_warning("Ops. Something is broken: {}".format(str(err)))
	return action_output

def parse_controller_name(cname):
	"""
	parse_controller_name(): It translates the passed controller name to the real file/class controller name
	"""
	controller_name = None
	for name in helper.get_package_modules(controllers):
		if cname.lower() == name.lower():
			controller_name = name
			break
	return controller_name
