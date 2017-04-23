from framework import Database as std

class Model:
	id = None

	def __init__(self, db_config, data = None):
		if data:
			self.db = std.Database(db_config)
			self.define_attributes(data)
		else:
			raise Exception("Error calling model '{}'. Model must receive some data.".format(self.__class__.__name__))

	def set_attribute(self, attribute_name, value):
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
		attributes = []
		for attr in self.attributes:
			attributes.append((attr, getattr(self, attr)))
		return dict(attributes)

	def define_attributes(self, data):
		"""
		define_attributes(): It assings the attribute values following the atributes set on attributes child attribute
		"""
		if 'id' in data:
			self.attributes.append('id')
		for attr in self.attributes:
			if attr in data:
				setattr(self, attr, data[attr])
			else:
				raise Exception("Error calling model '{}'. Attribute '{}' is missing on the passed data.".format(self.__class__.__name__, attr))

	
	def run_standard_query(self, script_name, attributes):
		"""
		run_standard_query(): It executes scripts placed on framework/db/scripts 
		"""
		cursor = self.db.execute(self.db.build_query(script_name, self.get_table_name(), attributes.keys()), attributes)
		return (self.db.conn, cursor)

	def save(self):
		"""
		save(): It saves the model content on db.
		If the Model::id is None a new record is created. Otherwise it'll try to update an existing record.
		"""
		if self.id is not None:
			conn, cursor = self.run_standard_query("update", self.get_attributes())
		else:
			conn, cursor = self.run_standard_query("create", self.get_attributes())
		return {
			"conn": conn,
			"cursor": cursor
		}

	def load(self, id):
		pass

	def destroy(self):
		pass

	def find(self):
		pass