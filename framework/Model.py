from framework.Database import Database

class Model:
	id = None

	def __init__(self, db_config, data = None):
		if data:
			self.db = Database(db_config)
			self.data = data
			self.define_attributes(data)
		else:
			raise Exception("Error calling model '{}'. Model must receive some data.".format(self.__class__.__name__))

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
		for attr in self.attributes:
			if attr in data:
				setattr(self, attr, data[attr])
			else:
				raise Exception("Error calling model '{}'. Attribute '{}' is missing on the passed data.".format(self.__class__.__name__, attr))

	
	def execute_standard_db_script(self, script_name):
		"""
		execute_standard_db_script(): It executes scripts placed on framework/db/scripts 
		"""
		cursor = self.db.execute(self.db.build_query(script_name, self.get_table_name(), self.get_attributes()), self.get_attributes())
		cursor.close()
		return self.db.conn

	def save(self):
		"""
		save(): It saves the model content on db.
		If the Model::id is None a new record is created. Otherwise it'll try to update an existing record.
		"""
		if self.id:
			return self.update()
		else:
			return self.create()

	def load(self, id):
		pass

	def destroy(self):
		pass

	def find(self):
		pass

	def create(self):
		return self.execute_standard_db_script("create")

	def update(self):
		return self.execute_standard_db_script("update")