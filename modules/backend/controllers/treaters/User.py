from framework import Treater as std

class User(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"email": 		["required", "email", "unique:email"],
					"password": 	["required", "maxlength:32", "minlength:8"],
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def update(self):
		return self.rules({
				"fields": {
					"id": 			["required"],
					"email": 		["required", "email", "unique:email"],
					"password": 	["required"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def delete(self):
		return self.rules({
				"fields": {
					"ids[]": ["required"]
				},
				"method": "post"
			})

	def fetch(self):
		return self.rules({
				"fields": {
					"start": ["required"],
					"limit": ["required"],
					"_":	["optional"]
				},
				"method": "get",
				"auth": []
			})
