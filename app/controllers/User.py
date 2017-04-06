from framework import Controller as std

class User(std.Controller):
	
	def register(self, request):
		return self.model().create()

	def make(self, request):
		return self.model().save(request)	


