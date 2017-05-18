from framework import Controller as std

class User(std.Controller):

	def access_levels(self):
		current_session = self.get_model('Session').get_current()
		if current_session is not None:
			return self.model().get_accesslevels(current_session['user_id'])
		else:
			return None

	def current(self):
		return self.get_model('Session').get_user()

	
