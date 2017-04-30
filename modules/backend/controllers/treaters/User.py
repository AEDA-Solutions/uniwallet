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

	def doit(self):
		return self.rules({
				"private": True
			})

	def make(self):
		return self.rules({
				"private": True
			})

	def foo(self):
		return self.rules({
				"method": "get",
				"auth": ["user"]
			})



