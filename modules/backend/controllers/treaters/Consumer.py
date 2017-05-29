from framework import Treater as std

class Consumer(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"fullname": 	["required"],
					"university": 	["required"],
					"cpf":			["required", "cpf", "unique:cpf"],
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
					"fullname": 	["required"],
					"university": 	["required"],
					"cpf":			["required", "cpf", "unique:cpf"],
					"email": 		["required", "email", "unique:email:User"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def set_accesses(self):
		return self.rules({
				"private": True
			})
