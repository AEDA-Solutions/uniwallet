from framework import Controller as std
from framework.Session import Session

class Session(std.Controller):
	
	def get_token(self):
		return self.model().generate_token()

	def login(self):
		users = self.model_class('User')(self.get_db_connection()).find([{'email': self.get_input('email'), 'password': self.get_input('password')}]).fetch()
		if len(users) > 0:
			session = self.model({'user_id': users[0]['id'], 'token': self.get_token(), 'ip': self.request.client_ip})
			session.make()
			return {"token": session.token}
		else:
			return self.forbid("Incorrect email or password")		

	def logout(self):
		return "ok"

	def oba(self):
		return "obaoba"