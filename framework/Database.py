import mysql.connector
from mysql.connector import errorcode
from helpers import debugger as debugger

class Database:
	def __init__(self, config):
		self.ok = True
		self.conn = mysql.connector.connect(**config)
		
	def get_script(self, script_name, path = "app/db/scripts", table_name = None):
		"""
		get_script(): It returns the sql script file content
		"""
		with open("{}/{}.sql".format(path, script_name), 'r') as file:
			if table_name:
				return file.read().replace("{table_name}", table_name)
			else:
				return file.read()
		
	def inject_data(self, query, data):
		"""
		inject_data(): It replaces the data on the script
		"""
		for key, value in data.items():
			if "{" + key + "}" in query: 
				query = query.replace("{}{}{}".format("{", key, "}"), str(value))
			else:
				raise Exception("Error calling model '{}'. SQL script '{}' is missing parameter '{}'.".format(self.__class__.__name__, query, key))
		return query

	def execute(self, query, data = None):
		"""
		execute(): It execute the selected file query
		"""
		cursor = self.conn.cursor()
		if data:
			sql = (self.inject_data(query, data))
		else:
			sql = (query)
		cursor.execute(sql)
		self.conn.commit()
		return cursor