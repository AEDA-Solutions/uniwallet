from framework import Treater as std

class Company(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"name": 		["required"],
					"cnpj":			["required", "cpf"],

					"email": 		["required", "email", "unique:email:User"],
					"password": 	["optional", "maxlength:32", "minlength:8"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def update(self):
		return self.rules({
				"fields": {
					"id": 			["required"],
					"name": 		["required"],
					"cnpj":			["required", "cpf"],

					"user_id": 		["required", "exists:id:User"],
					"email":		["required", "email", "unique:email:User:user_id"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
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

	def set_accesses(self):
		return self.rules({
				"private": True
			})

	def showall(self):
		return self.rules({


			#"auth": []
			})