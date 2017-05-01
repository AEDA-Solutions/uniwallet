from framework import Model as std
import uuid

class Auth(std.Model):

	attributes = ['user_id', 'token', 'ip']
	table_name = 'AuthSession'

	def generate_token(self):	
		return str(uuid.uuid4())

	def create_session(self):
		self.save().close()
		return self.token

	def destroy_session(self):
		pass

