from framework import Treater as std

class Static(std.Treater):
	def plain(self):
		if 'target' in self.request.GET:
			self.request.GET["target"][0].replace('..', '')
		else:
			self.forbid()
			return "Target is missing"
			

	def img(self):
		if 'target' in self.request.GET:
			self.request.GET["target"][0].replace('..', '')
		else:
			self.forbid()
			return "Target is missing"

 