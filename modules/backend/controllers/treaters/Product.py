from framework import Treater as std

class Product(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"number": 		["required"],
					"name": 		["required"],
					"price":		["required"],
					"description":	["required"],
					"category":		["required"],
					"company_id": 	["required", "exists:id:Company"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})
