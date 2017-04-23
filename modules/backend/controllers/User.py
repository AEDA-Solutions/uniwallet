from framework import Controller as std

class User(std.Controller):
	
	def register(self):
		query_result = self.model(self.get_request_parameters()).save()
		last_id = query_result["cursor"].lastrowid
		query_result["cursor"].close()
		query_result["conn"].close()
		return "Done: {} is the last id created".format(last_id)

	def update(self):
		query_result = self.model(self.get_request_parameters()).save()
		last_id = query_result["cursor"].rowcount
		query_result["cursor"].close()
		query_result["conn"].close()
		return "Done: {} rows affected".format(last_id)

	def doit(self):
		return self.request.parameters;

	def make(self):
		return "Making makers"

	def foo(self):
		return "Hello world"


