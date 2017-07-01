from framework import Treater as std

class Caio(std.Treater):
	def tirapontos(self):
		return self.rules({
				"fields": {
					"email": 		["required", "email"]
				},
				"method": "GET",
			})
