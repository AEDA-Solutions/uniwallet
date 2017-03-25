class Request:
	def __init__(self, env):
		self.env = env
		self.urn = env['PATH_INFO']
		self.urn_list = self.urn.strip('/').split('/')
		self.ok = len(self.urn_list) == 2
		if self.ok:
			self.resource = self.urn_list[0]
			self.action = self.urn_list[1]