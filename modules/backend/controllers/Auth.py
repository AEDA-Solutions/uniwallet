from framework import Controller as std
from framework.Auth import Auth

class Auth(std.Controller):
	
	def get_token(self):
		return self.model().generate_token()

	def login(self):
		connection = self.model_class('User')(self.get_db_connection()).find([{'email': self.get_input('email'), 'password': self.get_input('password')}])
		users = connection.fetch()	
		connection.close()
		if len(users) > 0:
			self.reset_session(users[0]['id'])
			return {"token": self.model({'user_id': users[0]['id'], 'token': self.get_token(), 'ip': self.request.client_ip}).create_session()}
		else:
			return self.forbid("Incorrect email or password")

	def reset_session(self, user_id):
		connection = self.model().destroy([{'user_id': user_id}, {'user_id': user_id}])
		connection.close()

	def logout(self):
		return "ok"