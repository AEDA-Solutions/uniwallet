from framework import Model as std
import uuid

class Session(std.Model):

	attributes = ['user_id', 'token', 'ip']
	table_name = 'AuthSession'

	def generate_token(self):	
		return str(uuid.uuid4())

	def make(self):
		self.destroy([{'user_id': self.user_id}]) #It removes previous user's session
		return self.save().close()

	def get_user_id_vinculated(self, token, ip):
		"""
		get_user_id_vinculated(): It gets the user id vinculated to the token
		"""
		sessions = self.find([{'token': token}]).fetch()
		if len(sessions) > 0:
			if sessions[0]['ip'] == ip:
				return sessions[0]['user_id']
			else:
				self.destroy([{'user_id': sessions[0]['user_id']}])
				return None
		else:
			return None


