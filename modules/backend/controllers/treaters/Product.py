from framework import Treater as std

class Product(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"company_id": 	["required", "exists:id:Company"],
					"number": 		["required"],
					"name": 		["required"],
					"description":	["required"],
					"category":		["required"],
					"price":	    ["required"],
					"quantity": 	["required", "integer"]
				},
				"method": "post",
				#"auth": ["manager", "client"],
			})

	def update(self):
		return self.rules({
				"fields": {
					"id":			["required", "exists:id"],
					"number": 		["required"],
					"name": 		["required"],
					"price":	 	["required"],
					"company_id":	["required", "exists:id:Company"],
					"description":	["required"],
					"category":		["required"],
				},
				"method": "post",
			})
