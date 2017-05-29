from framework import Session as std

class Session(std.Session):
	
	table_name = 'AuthSession'

	def get_logged_user(self):
		user_session = self.get_user()
		if user_session is not None:
			consumer = self.model(name = 'Consumer').find(join = [('User', 'user_id')], conditions = [('user_id', '=', user_session['user_id'])]).fetchone()
			if consumer is not None:
				return consumer
			else:
				company = self.model(name = 'Company').find(join = [('User', 'user_id')], conditions = [('user_id', '=', user_session['user_id'])]).fetchone()
				if company is not None:
					return company
				else:
					return None
		else:
			return None

