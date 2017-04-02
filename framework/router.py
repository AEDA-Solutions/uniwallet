from app import controllers
from framework import Response as default

"""
route

It delivers the request to the appropriate controller
"""
def route(request):
	if request.ok and hasattr(controllers, request.controller):
		ctrl = getattr(getattr(controllers, request.controller), request.controller)()
		return ctrl.action(request.action, request)
	else:
		return default.Response().make_warning("Controller '{}' unavailabe".format(request.controller))