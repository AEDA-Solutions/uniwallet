from framework import Treater as std

class Wallet(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"balance": 	["required"],
					"user_id":	["required", "exists:id:User"]
				},
				"method": "get",
				#"auth": ["manager", "client"]
			})
