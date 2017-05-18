from framework import Treater as std

class Sale(std.Treater):
	def create(self):
		return self.rules({
				"fields": {
					"consumer_id": ["required", "exists:id:Consumer"],
					"products[]": ["required", {
						"id": ["required", "exists:id:Product"],
						"quantity": ["required", "integer:unsigned"]
					}]					
				},
				"method": "post",
				"auth": ["company"]
			})