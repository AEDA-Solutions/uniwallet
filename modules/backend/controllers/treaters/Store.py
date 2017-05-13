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
