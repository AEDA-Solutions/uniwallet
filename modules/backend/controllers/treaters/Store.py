from framework import Treater as std

class Store(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"company_id": 	["required", "exists:id:Company"],
					"name": 		["required"],
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def append_product(self):
		return self.rules({
				"fields": {
					"store_id": 	["required", "exists:id:Store"],
					"product_id": 	["required", "exists:id:Product"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})