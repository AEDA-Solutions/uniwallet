from framework import Controller as std

class User(std.Controller):
	
	def register(self):
		connection = self.model(self.get_request_parameters()).save()
		last_id = connection.cursor.lastrowid
		connection.close()
		return "Done: {} is the last id created".format(last_id)

	def update(self):
		connection = self.model(self.get_request_parameters()).save()
		rowcount = connection.cursor.rowcount
		connection.close()
		return "Done: {} rows affected".format(rowcount)

	def delete(self):
		connection = self.model().destroy(list({'id': item} for item in self.get_request_parameters()['ids']))
		rowcount = connection.cursor.rowcount
		connection.close()
		return "Done: {} rows affected".format(rowcount)

	def fetch(self):
		connection = self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit'))
		records = connection.fetch(fields_to_ignore = ['password'])
		connection.close()
		return records

	def doit(self):
		return self.request.parameters

	def make(self):
		return "Making makers"

	def foo(self):
		return "Hello world"


