"""
Bootstrap

This function is where the whole thing gets started.
It means this function is invoked every time the server receives a request and then the system is built.
Here is where a database object is created to be passed to the system, as well.
In general the system is built differently for each request to serve exactly what the request is asking for.
"""

from framework.Router import Router
from framework.Request import Request
from framework.Response import Response
from framework.Database import Database
from app.db import config as DB

def bootstrap(env, meta):
	database = Database(DB.config())
	if(database.ok):
		request = Request(env)
		response = Router(request, database).route()
		database.conn.close()
	else:
		response = Response(code = 'Internal Server Error', body = "I'm sorry Dave. I've found a db connection issue. Try taking a look at the logs.")
	meta(response.status, response.headers)
	return [Response().prepare(response)]

