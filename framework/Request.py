from cgi import parse_qs, escape

class Request:
	def __init__(self, env):
		self.env = env
		self.urn = env['PATH_INFO']
		self.urn_list = self.urn.strip('/').split('/')
		self.ok = len(self.urn_list) == 2
		if self.ok:
			self.resource = self.urn_list[0]
			self.action = self.urn_list[1]
		self.POST = self.get_POST(env)

	def get_POST(self, env):
		request_body_size = 0
		try:
			request_body_size = int(env.get('CONTENT_LENGTH', 0))
		except (ValueError):
			request_body_size = 0

		request_body = env['wsgi.input'].read(request_body_size)
		return parse_qs(request_body)