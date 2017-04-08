from framework import Controller as std

class User(std.Controller):
	
	def register(self):
		return self.model().create()

	def make(self):
		return self.model().save(self.request)	

	def run(self):
		return "fdsafd"


