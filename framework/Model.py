from app.db import config as db

class Model:
	def __init__(self, db, data = None):
		self.conn = db.conn

	def sql_script(self, script_name, path = "app/db/scripts"):
		with open("{}/{}.sql".format(path, script_name), 'r') as file:
			return file.read()

	def save():
		pass

	def dump():
		pass
		