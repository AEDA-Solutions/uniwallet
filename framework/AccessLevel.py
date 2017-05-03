from framework import Model as std

class AccessLevel(std.Model):

	attributes = ['name', 'description']
	#table_name = 'AccessLevels'
	pivot_table_name = 'User_AccessLevel'

	def get_pivot_table_name(self):
		return self.pivot_table_name

	def make_name_list(self, records):
		"""
		make_name_list(): It receives the database access level records and turns it into a list containing the names of each record
		"""
		if len(records) > 0:
			return list(item['name'] for item in records)
		else:
			return []

	def get_from_user(self, user_id):
		"""
		get_from_user(): It returns a list containing the access levels related to the specified user_id
		"""
		connection = self.find(fields = [{'user_id': user_id}], table_name = self.get_pivot_table_name())
		user_vinculated_records = connection.fetch(close_connection = False)
		if len(user_vinculated_records) > 0:
			accesslevel_ids = list({'id': item['accesslevel_id']} for item in user_vinculated_records)
			return self.make_name_list(self.find(fields = accesslevel_ids).fetch())
		else:
			connection.close()
			return []
		
	def user_has(self, user_id, credential_list):
		"""
		user_has(): It checks if the user has at least one access level in common with credential_list
		"""
		if len(credential_list) > 0:
			if len(set(self.get_from_user(user_id)).intersection(credential_list)) > 0: 
				return True
			else:
				return False
		else:
			return True
			


	