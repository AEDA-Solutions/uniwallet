import re

class Middleware:

	def __init__(self, request):
		self.request = request

	def authorized(self):
		pass

	def validate(self):
		pass

	def check_item(self, request, rules):
		pass

	def rules():
		return {
			"email": r"^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$",
			"name": r".*",
			"fullname": r".*",
			"integer": r".*",
			"float": r".*",
			"required": r".*",
			"optional": r".*"
		}