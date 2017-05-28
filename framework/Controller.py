from framework.Core import Core
from framework.Response import Response
from helpers import dictionary, general
import importlib

class Controller(Core):

	def __init__(self, request):
		super().__init__(request)
		self.response = Response()

	def action(self, action_name):
		"""
		action(): It tries to call a method called 'action_name' from the current Controller object. Then it returns the output of that method.
		If that method is not found, it returns a warning.
		"""
		if hasattr(self, action_name) and callable(getattr(self, action_name)):
			self.response.body = getattr(self, action_name)()
			return self.response
		else:
			return Response(code = 'Not Found', body = "Action '{}' unavailable".format(action_name))

	def get_html(self, html_file_name):
		"""
		get_html(): It reads and returns the content of some html file placed on modules/{current_module}/html
		"""
		self.response_body_directly()
		return self.get_file("html/{}.html".format(html_file_name))

	def response_body_directly(self):
		"""
		response_body_directly(): It sets response.raw as True
		"""
		self.response.raw = True

	def forbid(self, message = None, code = 'Bad Request'):
		"""
		forbid(): It sets the code as 400 by default
		"""
		self.response.code = code
		if message:
			return message 

	def view(self, name = None, raw = True):
		"""
		view(): It returns a instance a of a model. If name is None the it will call the view with the current controller's name
		"""
		if raw:
			self.response_body_directly()
		return self.view(name = self.__class__.__name__ if name is None else name)

	def metadata(self, tuple_list):
		"""
		field(): It stringifies the dict attr
		"""
		fields = []
		for item in tuple_list:
			fields.append(tuple([item[0], "{}:{}".format(item[0], item[1])]))
		return fields

	def update(self):
		return "Done: {} rows affected".format(self.model().update(fields = self.get_request_parameters()).count_rows())

	def delete(self):
		return "Done: {} rows affected".format(self.model().destroy(list(('id', '=', item['id']) for item in self.get_input('data'))).count_rows())

	def fetch(self):
		return self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit')).fetch(fields_to_ignore = ['password'])



