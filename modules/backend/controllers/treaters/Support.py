from framework import Treater as std

class Support(std.Treater):
	
	def report(self):
		return self.rules({
				"fields": {
					"email": 	["required", "email"],
					"name": 	["required"],
					"content": 	["required"]
				},
				"method": "POST"
			})