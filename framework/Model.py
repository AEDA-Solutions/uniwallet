from framework.Database import Database
from app.db import config as DB

class Model:
	def __init__(self, data = None):
		if data:
			database = Database(DB.config())
			self.conn = database.conn
			self.data = data
			self.define_attributes(data)
			self.db_scripts = self.define_sql_scripts_path()
		else:
			raise Exception("Error calling model '{}'. Model must receive some data.".format(self.__class__.__name__))

	def define_sql_scripts_path(self):
		"""
		define_sql_scripts_path(): It fetches the sql scripts names
		"""
		return {
			'save': "save_{}".format(self.__class__.__name__.lower())
		}

	def get_attributes(self):
		"""
		get_attributes(): It returns a dict containing the model attributes
		"""
		attributes = []
		for attr in self.attributes:
			attributes.append((attr, getattr(self, attr)))
		return dict(attributes)

	def define_attributes(self, data):
		"""
		define_attributes(): It assings the attribute values following the atributes set on attributes child attribute
		"""
		for attr in self.attributes:
			if attr in data:
				setattr(self, attr, data[attr])
			else:
				raise Exception("Error calling model '{}'. Attribute '{}' is missing on the passed data.".format(self.__class__.__name__, attr))

	def sql_script(self, script_name, path = "app/db/scripts"):
		"""
		sql_script(): It returns the sql script file content
		"""
		with open("{}/{}.sql".format(path, script_name), 'r') as file:
			return file.read()
		
	def prepare_sql_script(self, sql_script_name, data):
		"""
		prepare_sql_script(): It replaces the data on the script
		"""
		file_content = self.sql_script(sql_script_name)
		for key, value in data.items():
			if "{" + key + "}" in file_content: 
				file_content = file_content.replace("{" + key + "}", value)
			else:
				raise Exception("Error calling model '{}'. SQL script '{}' is missing parameter '{}'.".format(self.__class__.__name__, sql_script_name, key))
		return file_content

	def execute_db_script(self, sql_script_name, data):
		"""
		execute_db_script(): It execute the selected file query
		"""
		cursor = self.conn.cursor()
		sql = (self.prepare_sql_script(sql_script_name, data))
		cursor.execute(sql)
		self.conn.commit()
		return cursor

	def save(self):
		"""
		save(): It saves the model content on db
		"""
		cursor = self.execute_db_script(self.db_scripts['save'], self.get_attributes())
		cursor.close()
		return self.conn
