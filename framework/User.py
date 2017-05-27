from framework import Model as std

class User(std.Model):

	attributes = ['name', 'email', 'password']

	def get_accesslevels(self, user_id):
		user_accesslevels = self.model(name = 'User_AccessLevel').find(join = [('AccessLevel', 'accesslevel_id'), ('User', 'User_AccessLevel.user_id')], conditions = [('User_AccessLevel.user_id', '=', user_id)])
		user_credentials = user_accesslevels.fetch(fields_mask = [('accesslevel_name', 'name')])
		if len(user_credentials) > 0:
			return list(item['name'] for item in user_credentials)
		else:
			return []

