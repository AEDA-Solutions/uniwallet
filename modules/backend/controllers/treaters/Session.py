from framework import Treater as std

class Session(std.Treater):
	def login(self):
		return self.rules({
				"fields": {
					#"email": 	["required", "email", "exists:email:User"],
					"email": 	["required", "email"],
					"password": ["required"]
				},
				"method": "post"
			})

	def logout(self):
		return self.rules({
				"method": "get"
			})

	def get_token(self):
		return self.rules({
				"private": True
			})

	def reset_session(self):
		return self.rules({
				"private": True
			})

	def fetch(self):
		return self.rules({
			"fields": {
				"start": ["required"],
				"limit": ["required"],
				"_":	["optional"]
			},
			"method": "get",
			"auth": ["registered"]
		})