from framework import Treater as std

class Auth(std.Treater):
	def login(self):
		return self.rules({
				"fields": {
					"email": 	["required", "email", "exists"],
					"password": ["required"]
				},
				"method": "post"
			})

	def logout(self):
		return self.rules({
				"fields": {
					"token": ["required"]
				},
				"method": "get"
			})