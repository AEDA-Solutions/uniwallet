from framework.Core import Core

class View(Core):

	def __init__(self, request):
		super().__init__(request)

	def get_html(self, html_file_name):
		"""
		get_html(): It reads and returns the content of some html file placed on modules/{current_module}/html
		"""
		return self.get_file("html/{}.html".format(html_file_name))