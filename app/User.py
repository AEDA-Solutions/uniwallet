from framework import Model as std
from framework.helpers import debugger as debugger

class User(std.Model):
	def __init__(self):
		super().__init__()

	def foo(self):
		if(self.db.ok):
			cursor = self.db.cnx.cursor()
			teste_data = ('Registro7')
			add_teste = ("INSERT INTO teste "
				"(data) "
				"VALUES ('{}')".format(teste_data))
			cursor.execute(add_teste)
			self.db.cnx.commit()
			cursor.close()
			self.db.cnx.close()
			return "Processed"
		else:
			return "DB error"

	def abc(self):
		return self.db.ok
		