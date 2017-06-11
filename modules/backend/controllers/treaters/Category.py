from framework import Treater as std

class Category(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"type": 		["required", "unique:type"],
					
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def update(self):
		return self.rules({
				"fields": {
					"id": 			["required"],
					"type": 		["required", "unique:type"],
					
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})