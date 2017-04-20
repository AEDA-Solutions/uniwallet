from framework import Treater as std

class Pages(std.Treater):

	def prepare_static(self):
		return self.rules({
				"private": True
			})

 