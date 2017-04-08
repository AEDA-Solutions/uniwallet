from framework import Treater as std

class User(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"firstname": ["required"],
					"lastname": ["required"],
					"email": ["required"],
					"login": ["required"],
					"password": ["required"],
					"ddd": ["optional"],
					"cellphone": ["optional"],
					"address": ["optional"],
					"city": ["optional"],
					"state": ["optional"],
					"neighborhhood": ["optional"],
					"cpf": ["optional"],
				},
				"auth": ["manager", "client"]
			})

	def make(self):
		return self.rules({
				"fields": {
					"name": ["required"]
				}
			})

	def run(self):
		return self.rules({
				"fields": {
					"addr": ["required"]
				}
			})



