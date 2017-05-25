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

	def changeselfpassword(self):
		current_user = self.current()
		user_data = self.get_model('User').find({('id', '=', current_user['id'])}).fetchone()
		if user_data is not None:
			user_model = self.get_model('User', data = user_data)
			user_model.password = self.get_input('password')
			return "{} linhas foram alteradas".format(user_model.save().count_rows())
		else:
			return "Usuário não encontrado"


	
