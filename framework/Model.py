from framework import Database as std
from framework.Connection import Connection
from framework.QueryBuilder import QueryBuilder

class Model:
	id = None

	def __init__(self, database, data = None, table_name = None):
		self.db = database
		if data:
			self.define_attributes(data)
		#else:
		#	raise Exception("Error calling model '{}'. Model must receive some data.".format(self.__class__.__name__))

	def build_query(self):
		return QueryBuilder()

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
		return Connection(self.db.conn, cursor)

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

	def update(self, fields = None, table_name = None):
		"""
		update(): It updates a db record from the passed data (id is required)
		"""
		query = """

			UPDATE {table_name} SET {fields} WHERE id='{id}'

			""".format(table_name = self.get_table_name() if table_name is None else table_name, fields = ", ".join("{}={}".format(item, "'{" + item + "}'") for item in self.attributes), id = self.id)

		return self.run_query(query, self.get_attributes() if fields is None else fields)

	def create(self, table_name = None):
		"""
		create(): It creates a new db record from passed data
		"""
		query = (self.build_query()
			.table(self.get_table_name() if table_name is None else table_name)
			.insert([self.get_attributes()])
			.get())
		return self.run_query(query)

	def destroy(self, fields, table_name = None):
		"""
		destroy(): It removes records from db from the ids passed (ids must be a list)
		"""
		query = (self.build_query()
			.table(self.get_table_name() if table_name is None else table_name)
			.delete()
			.where(raw = 0 if fields is None or len(fields) == 0 else " OR ".join(list((0 if item is None else " AND ".join(list("{}={}{}{}".format(elem, "'", item[elem], "'") for elem in item))) for item in fields)))
			.get())

		return self.run_query(query)

	def find(self, fields = None, fields_to_ignore = None, start_from = 0, limit = 18446744073709551615, target_fields = ["*"], table_name = None):
		"""
		find(): It finds records with the specified fields according the referred limits
		"""
		query = """

			SELECT {target_fields} FROM {table_name} WHERE {fields} AND {fields_to_ignore} LIMIT {start_from},{limit};

			""".format(target_fields = ", ".join(item for item in target_fields),
					   table_name = self.get_table_name() if table_name is None else table_name, 
					   fields = 1 if fields is None or len(fields) == 0 else " OR ".join(list((1 if item is None else " AND ".join(list("{}={}{}{}".format(elem, "'", item[elem], "'") for elem in item))) for item in fields)), 
					   fields_to_ignore = 1 if fields_to_ignore is None or len(fields_to_ignore) == 0 else " OR ".join(list((1 if item is None else " AND ".join(list("{}<>{}{}{}".format(elem, "'", item[elem], "'") for elem in item))) for item in fields_to_ignore)),
					   start_from = start_from,
					   limit = limit)

		return self.run_query(query)

