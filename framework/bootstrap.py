"""
Bootstrap

This function is where the whole thing gets started.
It means this function is invoked every time the server receives a request and then the system is built.
In general the system is built differently for each request to serve exactly what the request is asking for.
"""

from framework.Router import Router
from framework.Request import Request
from app.controllers import User
from framework.helpers.environment import dump_env

def bootstrap(env, meta):
	request = Request(env)
	response = Router(request).route()
	meta(response.status, response.headers)
	return [response.get_body()]