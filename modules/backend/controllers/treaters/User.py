from framework import Treater as std

class User(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"firstname": ["required"],
					"lastname": ["required"],
					"email": ["required"],
					"university": ["required"],
					"password": ["required"]
				},
				"method": "post"
				#"auth": ["manager", "client"]
			})

	def doit(self):
		return self.rules({
				"private": True
			})

	def make(self):
		return self.rules({
				"private": True
			})



