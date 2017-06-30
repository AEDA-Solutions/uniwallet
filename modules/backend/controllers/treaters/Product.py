from framework import Treater as std

class Product(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"company_id": 	["required", "exists:id:Company"],
					"name": 		["required"],
					"description":	["required"],
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
					"name": 		["required"],
					"price":	 	["required"],
					"company_id":	["required", "exists:id:Company"],
					"description":	["required"],
					"quantity": 	["required", "integer"]
				},
				"method": "post",
			})

	def filter(self):
		return self.rules({
				"fields": {
					"company_id": ["optional", "integer", "exists:id:Company"],
					"price": ["optional", "integer"],
					"category": ["optional", "exists:id:Category"]
				}
			})
