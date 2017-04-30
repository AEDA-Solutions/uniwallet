from framework import Model as std
import uuid

class Auth(std.Model):

	attributes = ['user_id', 'token', 'ip']
	table_name = 'AuthSession'

	def generate_token(self):	
		return uuid.uuid4()

	def create_session(self):
		pass

	def destroy_session(self):
		pass

