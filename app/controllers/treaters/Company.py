from framework import Treater as std

class Company(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"compname": ["required"],
					"email": ["required"],
					"location": ["required"],
					"password": ["required"],
					"phone": ["required"],
					"cnpj": ["optional"]

				},
				#"auth": ["manager", "client"]
			})



