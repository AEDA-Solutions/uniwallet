from framework import Treater as std

class User_AccessLevel(std.Treater):
	
	def register(self):
		return self.rules({
				"fields": {
					"user_id": 			["required", "exists:id:User"],
					"accesslevel_id": 	["required", "exists:id:AccessLevel"]
				},
				"method": "post",
				"auth": ["god"]
			})

