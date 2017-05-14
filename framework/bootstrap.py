"""
Bootstrap

This function is where the whole thing gets started.
It means this function is invoked every time the server receives a request and then the system is built.
Here is where a database object is created to be passed to the system, as well.
In general the system is built differently for each request to serve exactly what the request is asking for.
"""

from framework.Application import Application
from framework.Request import Request
from framework.Response import Response
from helpers import debugger as debugger
import traceback

def bootstrap(environment, meta):
	try:
		response = Application(Request(environment)).run()
	except Exception as e:
		debugger.applog(traceback.format_exc())
		response = Response(code = 'Internal Server Error', body = "I'm sorry Dave, I'm afraid I can't do that ({})".format(str(e)))
	
	server_output = response.prepare()
	meta(response.status, response.headers)
	return [server_output]

