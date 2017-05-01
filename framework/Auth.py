from framework import Model as std
import uuid

class Auth(std.Model):

	attributes = ['user_id', 'token', 'ip']
	table_name = 'AuthSession'

	def generate_token(self):	
		return str(uuid.uuid4())

	def create_session(self):
		self.destroy([{'user_id': self.user_id}]) #It removes previous user's session
		return self.save().close()

