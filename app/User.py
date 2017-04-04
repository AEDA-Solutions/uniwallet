from framework import Model as std
from framework.helpers import debugger as debugger

class User(std.Model):

	def foo(self):

		cursor = self.conn.cursor()

		script = get_script()

		dados = ('guilhere', 25, 'email')

		db_command = (script.format(dados))
		#pegar script com db

		retorno = cursor.execute(db_command)
		self.conn.commit()
		
		cursor.close()
		return "Pronto"

	def abc(self):
		return "abc"

	def doit(self):
		return "Hello bitch"
		