import mysql.connector
from mysql.connector import errorcode
from framework.helpers import debugger as debugger

class Connection:
	def __init__(self, config):
		self.ok = True
		try:
			self.cnx = mysql.connector.connect(**config)
		except mysql.connector.Error as err:
			self.ok = False
			self.register_errors(err)
			self.cnx.close()

	def register_errors(self, err):
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			debugger.applog("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			debugger.applog("Database does not exist")
		else:
			debugger.applog(err)
		