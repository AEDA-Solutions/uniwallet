from framework import Middleware as std

class User(std.Middleware):
	def register(self, request):
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
			}, request)



