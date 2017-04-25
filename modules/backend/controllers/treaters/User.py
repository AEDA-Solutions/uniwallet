from framework import Treater as std

class User(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"firstname": 	["required"],
					"lastname": 	["required"],
					"email": 		["required", "email", "unique"],
					"university": 	["required"],
					"password": 	["required"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def update(self):
		return self.rules({
				"fields": {
					"id": 			["required"],
					"firstname": 	["required"],
					"lastname": 	["required"],
					"email": 		["required", "email", "unique"],
					"university": 	["required"],
					"password": 	["required"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def doit(self):
		return self.rules({
				"private": True
			})

	def make(self):
		return self.rules({
				"private": True
			})

	def foo(self):
		return self.rules({
				"method": "get",
				"auth": ["user"]
			})



