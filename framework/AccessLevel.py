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
		
	def user_has(self, user_id, credential_list):
		"""
		user_has(): It checks if the user has at least one access level in common with credential_list
		"""
		query = (self.build_query()
			.table(self.get_table_name())
			.select()
			.join(table_name = self.get_pivot_table_name(), conditions = ['{}.id'.format(self.get_table_name()), '=', '{}.accesslevel_id'.format(self.get_pivot_table_name())])
			.join(table_name = 'Users', conditions = [['{}.user_id'.format(self.get_pivot_table_name()), '=', 'Users.id']])
			.where(raw = "Users.id = '{}'".format(user_id))
			.get())

		if len(credential_list) > 0:
			if len(set(self.make_name_list(self.run_query(query).fetch())).intersection(credential_list)) > 0: 
				return True
			else:
				return False
		else:
			return True
			


	