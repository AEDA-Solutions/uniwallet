import mysql.connector
from mysql.connector import errorcode
from framework.helpers import debugger as debugger

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
		
	def inject_data_on_query(self, query, data):
		"""
		inject_data_on_query(): It replaces the data on the script
		"""
		for key, value in data.items():
			if "{" + key + "}" in query: 
				query = query.replace("{}{}{}".format("{", key, "}"), str(value))
			else:
				raise Exception("Error calling model '{}'. SQL script '{}' is missing parameter '{}'.".format(self.__class__.__name__, query, key))
		return query

	def execute(self, query, data):
		"""
		execute(): It execute the selected file query
		"""
		cursor = self.conn.cursor()
		sql = (self.inject_data_on_query(query, data))
		cursor.execute(sql)
		self.conn.commit()
		return cursor

	def build_query(self, script_name, table_name, data):
		"""
		build_query(): It prepares the query replacing {fields}, {data}, {field_to_set}, snippets
		It is used just for the framework itself.
		"""
		query = self.get_script(script_name, "framework/db/scripts", table_name)
		fields = []
		quoted_fields = []
		fields_to_set = []
		for key, value in data.items():
			fields.append(key)
			quoted_fields.append("'{" + key + "}'")
			fields_to_set.append("{}={}{}{}".format(key, "'{", key, "}'"))
		return query.replace("{fields}", ", ".join(fields)).replace("{data}", ", ".join(quoted_fields)).replace("{fields_to_set}", ", ".join(fields_to_set))
