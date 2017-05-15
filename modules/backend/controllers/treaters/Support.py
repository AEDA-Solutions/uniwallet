from framework import Treater as std

class Support(std.Treater):
	
	def report(self):
		return self.rules({
				"fields": {
					"email": 	["required", "email"],
					"name": 	["required"],
					"content": 	["required"]
				},
				"method": "POST"
			})

	def foo(self):
		return self.rules({
				"fields": {
					"p": ["required", {
							"name": ["required"],
							"idade": ["required", "integer"],
							"lista": ["required", {
								"ids[]": ["required", "integer"]
							}]
						}],
					"q[]": ["required", "cpf"],
					"baz[]": ["required", {
						"id": ["required", "integer"]
					}],
					"yep": ["required"]
				},
				"method": "POST"
			})