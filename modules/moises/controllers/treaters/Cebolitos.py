from framework import Treater as std

class Cebolitos(std.Treater):

	def salvar(self):
		return self.rules({
				"fields":{
					"nome": ["required"],
					"email": ["required"],
					"senha": ["required"]
				},
				"method": "post"
			})