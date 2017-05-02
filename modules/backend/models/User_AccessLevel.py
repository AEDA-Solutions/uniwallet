from framework import Model as std

class User_AccessLevel(std.Model):
	
	attributes = ['user_id', 'accesslevel_id']
	table_name = 'User_AccessLevel'

	#Special save method for avoiding repeated registers
	def check_save(self):
		connection = self.find([self.get_attributes()])
		if len(connection.fetch(close_connection = False)) > 0:
			connection.close()
			return 0;
		else:
			return self.save().count_rows()