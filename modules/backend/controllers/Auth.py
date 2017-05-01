from framework import Controller as std
from framework.Auth import Auth

class Auth(std.Controller):
	
	def get_token(self):
		return self.model().generate_token()

	def login(self):
		users = self.model_class('User')(self.get_db_connection()).find([{'email': self.get_input('email'), 'password': self.get_input('password')}]).fetch()
		if len(users) > 0:
			auth = self.model({'user_id': users[0]['id'], 'token': self.get_token(), 'ip': self.request.client_ip})
			auth.create_session()
			return {"token": auth.token}
		else:
			return self.forbid("Incorrect email or password")		

	def logout(self):
		return "ok"