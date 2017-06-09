from framework import Model as std
from helpers import crypt

class User(std.Model):

	attributes = ['name', 'email', 'password']

	def get_accesslevels(self, user_id):
		user_accesslevels = self.model(name = 'User_AccessLevel').find(join = [('AccessLevel', 'accesslevel_id'), ('User', 'User_AccessLevel.user_id')], conditions = [('User_AccessLevel.user_id', '=', user_id)])
		user_credentials = user_accesslevels.fetch(aliases = [('accesslevel_name', 'name')])
		if len(user_credentials) > 0:
			return list(item['name'] for item in user_credentials)
		else:
			return []

	def save(self):
		self.password = crypt.make_hash(self.password)
		return super().save()

	def checkout(self, email, passw):
		return self.model().find([('email', '=', email), ('password', '=', crypt.make_hash(passw))]).fetchone()


	
