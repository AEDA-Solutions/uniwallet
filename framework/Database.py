import mysql.connector
from mysql.connector import errorcode
from framework.helpers import debugger as debugger

class Database:
	def __init__(self, config):
		self.ok = True
		try:
			self.conn = mysql.connector.connect(**config)
		except mysql.connector.Error as err:
			self.ok = False
			self.register_errors(err)

	def register_errors(self, err):
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			debugger.applog("Something is wrong with your user name or password", "database.log")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			debugger.applog("Database does not exist", "database.log")
		else:
			debugger.applog(err, "database.log")
		