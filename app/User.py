from framework import Model as std
from framework.helpers import debugger as debugger

class User(std.Model):

	def foo(self):

		cursor = self.conn.cursor()
		teste_data = ('Registro9')
		add_teste = ("INSERT INTO teste "
			"(data) "
			"VALUES ('{}')".format(teste_data))
		cursor.execute(add_teste)
		self.conn.commit()
		cursor.close()
		return "Stored"

	def abc(self):
		return "abc"

	def doit(self):
		return "Hello bitch"
		