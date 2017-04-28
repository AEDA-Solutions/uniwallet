from framework import Database as std

class Model:
	id = None

	def __init__(self, database, data = None):
		self.db = database
		if data:
			self.define_attributes(data)
		#else:
		#	raise Exception("Error calling model '{}'. Model must receive some data.".format(self.__class__.__name__))

	def set_attribute(self, attribute_name, value):
		"""
		set_attribute() It defines a new attribute on the model
		"""
		self.attributes.append(attribute_name)
		setattr(self, attribute_name, value)

	def get_table_name(self):
		"""
		get_table_name() It returns the table name.
		"""
		if hasattr(self, "table_name"):
			return self.table_name
		else:
			return self.__class__.__name__ + 's';

	def get_attributes(self):
		"""
		get_attributes(): It returns a dict containing the model attributes
		"""
		return dict((item, getattr(self, item)) for item in self.attributes)

	def define_attributes(self, data):
		"""
		define_attributes(): It assings the attribute values following the atributes set on attributes child attribute
		"""
		if 'id' in data:
			self.attributes.append('id')
		for attr in self.attributes:
			if attr in data.keys():
				setattr(self, attr, data[attr])
			else:
				raise Exception("Error calling model '{}'. Attribute '{}' is missing on the passed data.".format(self.__class__.__name__, attr))

	def run_query(self, query, data = None):
		"""
		run_standard_query(): It executes scripts placed on framework/db/scripts 
		"""
		cursor = self.db.execute(query, data)
		return Model.Connection(self.db.conn, cursor)

	def save(self):
		"""
		save(): It saves the model content on db.
		If the Model::id is None a new record is created. Otherwise it'll try to update an existing record.
		"""
		if self.id is not None:
			connection = self.update()
		else:
			connection = self.create()

		return connection

	def load(self):
		pass

	def update(self):
		"""
		update(): It updates a db record from the passed data (id is required)
		"""
		query = """

			UPDATE {table_name} SET {fields} WHERE id='{id}'

			""".format(table_name = self.get_table_name(), fields = ", ".join("{}={}".format(item, "'{" + item + "}'") for item in self.attributes), id = self.id)

		return self.run_query(query, self.get_attributes())

	def create(self):
		"""
		create(): It creates a new db record from passed data
		"""
		query = """

			INSERT INTO {table_name} ({fields}) VALUES ({data})

			""".format(table_name = self.get_table_name(), fields = ", ".join(self.attributes), data = ", ".join("'{" + item + "}'" for item in self.attributes))
		
		return self.run_query(query, self.get_attributes())

	def destroy(self, ids):
		"""
		destroy(): It removes records from db from the ids passed (ids must be a list)
		"""
		query = """

			DELETE FROM {table_name} WHERE id IN ({ids});

			""".format(table_name = self.get_table_name(), ids = ", ".join("'" + item + "'" for item in ids))
		
		return self.run_query(query)

	def find(self):
		pass

	class Connection:
		
		def __init__(self, connection, cursor):
			self.connection = connection
			self.cursor = cursor

		def close(self):
			self.connection.close()
			self.cursor.close()
