from framework import Controller as std
from framework.Auth import Auth

class Auth(std.Controller):
	
	def login(self):
		self.model({'user_id': 1, 'token': '456789fimdsiag7980-i', 'ip': '10.10.10.10'}).save().close()
		return "ok"

	def logout(self):
		return "ok"