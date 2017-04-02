from app import controllers
from framework import Response as default

"""
route

It routes the requests.
"""
def route(request):
	if request.ok and hasattr(controllers, request.resource):
		ctrl = getattr(getattr(controllers, request.resource), request.resource)()
		return ctrl.action(request.action, request)
	else:
		return default.Response().make_warning("Route {} unavailabe".format(request.urn))