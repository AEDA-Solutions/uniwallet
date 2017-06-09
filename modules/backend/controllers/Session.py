from . import Controller as std
from framework.Session import Session
from helpers import crypt

class Session(std.Controller):
	
	def get_token(self):
		return self.model().generate_token()

	def login(self):
		user = self.model(name = 'User').checkout(self.get_input('email'), self.get_input('password'))
		if user is not None:
			session = self.model(data = {'user_id': user['id'], 'token': self.get_token(), 'ip': self.request.client_ip})
			session.make()
			return {"token": session.token}
		else:
			return self.forbid("Incorrect email or password")


	def logout(self):
		return "Done: {} session destroyed".format(self.model().close())

	def fetch(self):
		return self.model().find(join = [('User', 'user_id')], start_from = self.get_input('start'), limit = self.get_input('limit')).fetch(fields_to_ignore = ['ip', 'user_password', 'user_created_at', 'created_at'])

	def fetchadmin(self):
		mask = self.metadata([('id', ':::hide'), ('user_name', ':Usuário::noneditable'), ('token', ':Token::noneditable'), ('ip', ':IP::noneditable')])
		return (self.model().find(join=[('User', 'user_id')], start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))