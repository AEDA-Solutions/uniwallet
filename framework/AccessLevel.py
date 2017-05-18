from framework import Model as std

class AccessLevel(std.Model):

	attributes = ['name', 'description']

	def make_name_list(self, records):
		"""
		make_name_list(): It receives the database access level records and turns it into a list containing the names of each record
		"""
		if len(records) > 0:
			return list(item['name'] for item in records)
		else:
			return []
	
	def get_user_credentials(self, user_id):
		user_accesslevels = self.get_model('User_AccessLevel').find(join = [('AccessLevel', 'accesslevel_id'), ('User', 'User_AccessLevel.user_id')], conditions = [('User_AccessLevel.user_id', '=', user_id)])
		user_credentials = self.make_name_list(user_accesslevels.fetch(fields_mask = [('accesslevel_name', 'name')]))
		return user_credentials

	def user_has(self, user_id, credential_list):
		"""
		user_has(): It checks if the user has at least one access level in common with credential_list
		"""
		user_credentials = self.get_model('User').get_accesslevels(user_id)

		if len(user_credentials) > 0:
			if len(set(user_credentials).intersection(credential_list)) > 0: 
				return True
			else:
				return False
		else:
			return True
			


	