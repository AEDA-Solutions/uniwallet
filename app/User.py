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

	def save(self, request):
		cursor = self.conn.cursor()
		sql = (self.sql_script("save_user").format(request.body['name'], "Sá", "gresendesa", "123456", "61", "123", "Sobradinho", "Sobradinho", "Sobradinho", "Meus amigos", "54353", "gresendesa@gmail.com"))
		cursor.execute(sql)
		self.conn.commit()
		cursor.close()
		return "Stored motherfucker"
		