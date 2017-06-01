from framework import Treater as std

class Purchase(std.Treater):
	def create(self):
		return self.rules({
				"fields": {
					"company_id": ["required", "exists:id:Company"],
					"products[]": ["required", {
						"id": ["required", "exists:id:Product"],
						"quantity": ["required", "integer:unsigned"]
					}]					
				},
				"method": "post",
				"auth": ["consumer"]
			})