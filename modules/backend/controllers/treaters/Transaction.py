from framework import Treater as std

class Transaction(std.Treater):
	def save(self):
		return self.rules({
				"fields": {
					"operation": 	["required"],
					"value": 	["required"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})