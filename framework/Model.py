from framework.Database import Database
from app.db import config as DB

class Model:
	def __init__(self, data = None):
		database = Database(DB.config())
		self.conn = database.conn

	def sql_script(self, script_name, path = "app/db/scripts"):
		with open("{}/{}.sql".format(path, script_name), 'r') as file:
			return file.read()

	def save():
		pass

	def dump():
		pass
		