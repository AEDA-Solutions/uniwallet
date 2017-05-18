from framework import Model as std
import uuid

class Session(std.Model):

	attributes = ['user_id', 'token', 'ip']

	def generate_token(self):	
		return str(uuid.uuid4())

	def make(self):
		self.destroy([('user_id', '=', self.user_id)]) #It removes previous user's session
		return self.save().close()

	def close(self):
		return self.destroy(conditions = [('token', '=', self.request.authorization.content)]).count_rows()

	def get_user(self):
		current_session = self.get_current()
		if current_session is not None:
			return self.get_model('User').find([('id', '=', current_session['user_id'])]).fetchone(fields_to_ignore = ['password'])
		else:
			return None

	def get_current(self):
		return self.find([('token', '=', self.request.authorization.content)]).fetchone()


