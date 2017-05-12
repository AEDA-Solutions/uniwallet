from framework import Treater as std

class Company(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"name": 		["required"],
					"cnpj":			["required", "cpf"],

					"email": 		["required", "email", "unique:email:User"],
					"password": 	["required", "maxlength:32", "minlength:8"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def update(self):
		return self.rules({
				"fields": {
					"id*": 			["required"],
					"name": 		["required"],
					"cnpj":			["required", "cpf"]
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

	def set_accesses(self):
		return self.rules({
				"private": True
			})