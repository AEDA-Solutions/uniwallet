from framework import Treater as std

class Product(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"product_id": 	["required"],
					"name": 		["required"],
					"price":		["required"],
					"description":	["required"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})
