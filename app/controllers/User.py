from framework import Controller as std

class User(std.Controller):
	def sample(self, request):
		if 'name' in request.body:
			return request.body['name']
		else:
			return "attribute 'name' not found: {}".format(self.model().foo())

	def abc(self, request):
		user = model.User(self.db)
		return "Abc {}".format("ok")

	def run(self, request):
		return self.model().foo()

