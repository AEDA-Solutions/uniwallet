from framework import Treater as std

class Test(std.Treater):
	def coisa(self):
		return self.rules({
				"fields": {
					"name": ["required"],
					"teste": "required"
				},
				"auth": ["manager", "client"]
			})

