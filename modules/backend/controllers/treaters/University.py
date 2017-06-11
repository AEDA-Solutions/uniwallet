from framework import Treater as std

class University(std.Treater):
	def register(self):
		return self.rules({
				"fields": {
					"name": 		["required", "unique:name"],
					"abbreviation":	["required", "unique:abbreviation"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def update(self):
		return self.rules({
				"fields": {
					"id": 			["required"],
					"name": 		["required", "unique:name"],
					"abbreviation":	["required", "unique:abbreviation"]
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})

	def fetch(self):
		"""
		fetch(): It implements a default validator for the fetch request
		"""
		return self.rules({
				"fields": {
					"start": 	["required", "integer:unsigned"],
					"limit": 	["required", "integer:unsigned"],
					"_":		["optional"]
				},
				"method": "get",
				"auth": []
			})