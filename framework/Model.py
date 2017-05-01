from framework import Database as std
import helpers

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

	def destroy(self, fields):
		"""
		destroy(): It removes records from db from the ids passed (ids must be a list)
		"""
		
		query = """

			DELETE FROM {table_name} WHERE {fields};

			""".format(table_name = self.get_table_name(),
					   fields = 0 if fields is None or len(fields) == 0 else " OR ".join(list((0 if item is None else " AND ".join(list("{}={}{}{}".format(elem, "'", item[elem], "'") for elem in item))) for item in fields)))
		
		return self.run_query(query)


	def find(self, fields = None, fields_to_ignore = None, start_from = 0, limit = 18446744073709551615, target_fields = ["*"]):
		"""
		find(): It finds records with the specified fields according the referred limits
		"""
		query = """

			SELECT {target_fields} FROM {table_name} WHERE {fields} AND {fields_to_ignore} LIMIT {start_from},{limit};

			""".format(target_fields = ", ".join(item for item in target_fields),
					   table_name = self.get_table_name(), 
					   fields = 1 if fields is None or len(fields) == 0 else " OR ".join(list((1 if item is None else " AND ".join(list("{}={}{}{}".format(elem, "'", item[elem], "'") for elem in item))) for item in fields)), 
					   fields_to_ignore = 1 if fields_to_ignore is None or len(fields_to_ignore) == 0 else " OR ".join(list((1 if item is None else " AND ".join(list("{}<>{}{}{}".format(elem, "'", item[elem], "'") for elem in item))) for item in fields_to_ignore)),
					   start_from = start_from,
					   limit = limit)

		return self.run_query(query)

	class Connection:
		"""
		class Connection: It represents the connection artefact that must be returned to the controller after a database transaction
		"""
		
		def __init__(self, connection, cursor):
			self.connection = connection
			self.cursor = cursor

		def close(self):
			"""
			close(): It closes both cursor and database connection
			"""
			self.cursor.close()
			self.connection.close()

		def fetch(self, fields_to_ignore = []):
			"""
			fetch_records_as_dict(): It returns a list of dict from the got data
			"""
			raw_records = self.cursor.fetchall()
			records = []
			for record_tuple in raw_records:
				records.append(helpers.general.remove_fields_from_dict(dict(zip(self.cursor.column_names, record_tuple)), fields_to_ignore))
			return records

