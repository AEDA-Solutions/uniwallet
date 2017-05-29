from framework import Treater as std

class Transaction(std.Treater):
	def save(self):
		return self.rules({
				"fields": {
					"destiny": ["required"], #id da wallet
					"operation": 	["required"], 
					"value": 	["required"] #POSITIVO ou Negativo
				},
				"method": "post",
				#"auth": ["manager", "client"]
			})