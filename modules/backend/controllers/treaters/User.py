from framework import Treater as std

class User(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"fullname": 	["required"],
					"email": 		["required", "email", "unique:email"],
					"university": 	["required"],
					"password": 	["required", "maxlength:8", "minlength:8"],
					"cpf":			["required", "cpf"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def update(self):
		return self.rules({
				"fields": {
					"id*": 			["required"],
					"fullname": 	["required"],
					"email": 		["required", "email", "unique:email"],
					"university": 	["required"],
					"password": 	["required"],
					"cpf":			["required", "cpf"]
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
