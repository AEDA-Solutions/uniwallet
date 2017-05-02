from framework import Treater as std

class AccessLevel(std.Treater):
	
	def register(self):
		return self.rules({
				"fields": {
					"name": 		["required", "unique:name"],
					"description": 	["required"]
				},
				"method": "post"
			})

	def empower(self):
		return self.rules({
				"fields": {
					"user_id": 			["required", "exists:id:User"],
					"accesslevel_id": 	["required", "exists:id:AccessLevel"]
				},
				"method": "post"
			})

	def fetch(self):
		return self.rules({
			"fields": {
				"start": ["required"],
				"limit": ["required"]
			},
			"method": "get"
		})	



