from framework import Treater as std

class App2(std.Treater):

	def prepare_static(self):
		return self.rules({
				"private": True
			})