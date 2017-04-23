from framework import Treater as std

class Transaction(std.Treater):
	def save(self):
		return self.rules({
				"fields": {
					"id": 	["required"],
					"operation": 	["required"]
				},
				"method": "get",
				#"auth": ["manager", "client"]
			})