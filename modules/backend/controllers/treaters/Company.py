from framework import Treater as std

class Company(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"compname": ["required"],
					"email": 	["required", "email", "unique"],
					"location": ["required"],
					"password": ["required"],
					"phone": 	["required"],
					"cnpj": 	["optional"]

				},
				"method": "post"
				#"auth": ["manager", "client"]
			})



