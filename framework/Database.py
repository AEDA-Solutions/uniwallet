import mysql.connector
from mysql.connector import errorcode
from framework.helpers import debugger as debugger

class Database:
	def __init__(self, config):
		self.ok = True
		self.conn = mysql.connector.connect(**config)
		