from app import controllers
from framework import Response as default

"""
route

It routes the requests. 
It means, if the system is separated into parts that do specific things, 
and as usually a request asks for just one of those things,
these requests must be guided to the right resource. So read 'to guide' as
making a route to something.

Each request has a URI what is composed by both URL and URN.
This function, as expected, analizes just the URN to figure out what resouce the request is trying to reach.

This function requires URNs to follow this structure:
{controller_name}/{action_name}

{controller_name} stands for a name of an existent app controller.
{action_name} must receive the name a method of the controller reffered by {controller_name}.

It means that the request must be redirected and processed by the method {action_name} that belongs to the controller {controller_name}

The route function returns a Response object.
"""
def route(request):
	if request.ok and hasattr(controllers, request.resource):
		ctrl = getattr(getattr(controllers, request.resource), request.resource)()
		return ctrl.action(request.action)
	else:
		return bad_route(request)

def bad_route(request):
	response = default.Response()
	response.ok = False
	response.body = "Route {} unavailabe".format(request.urn)
	return response