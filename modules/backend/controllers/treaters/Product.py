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

	def update(self):
		return self.rules({
				"fields": {
					"id":			["required", "exists:id"],
					"number": 		["required"],
					"name": 		["required"],
					"price":	 	["required"],
					"company_id":	["required", "company_id", "unique:company_id"],
					"description":	["required"],
					"category":		["required"]
				},
				"method": "post",
			})
