from framework import Model as std
from framework.helpers import debugger as debugger

class User(std.Model):

	def create(self):
		cursor = self.conn.cursor()
		#script = get_script()
		self.conn.commit()
		cursor.close()
		#return "Sucessfully created"

		return self.sql_script("script_create_tables")

		