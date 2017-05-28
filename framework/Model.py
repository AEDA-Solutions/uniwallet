from framework.Core import Core
from framework.Connection import Connection
from framework.QueryBuilder import QueryBuilder

class Model(Core):
	id = None

	def __init__(self, request, data = None):
		super().__init__(request)
		self.db = self.get_db_connection()
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

	def get_fields(self):
		return self.attributes + ['id', 'created_at']

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

	
	def fill(self, data):
		"""
		fill(): It fills the current object with the passed data dictionary
		"""
		for item in data:
			if item != 'id' and item in self.attributes:
				setattr(self, item, data[item])
		return self

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

	def load(self, id):
		"""
		load(): It returns a filled object from the id
		"""
		data = self.find(conditions = [('id', '=', id)]).fetchone()
		return self.model(data = data)

	def update(self, fields = None, table_name = None):
		"""
		update(): It updates a db record from the passed data (id is required)
		"""
		data = fields if fields is not None else self.get_attributes()
		query = (self.build_query()
			.table(self.get_table_name() if table_name is None else table_name)
			.update(values_dict = data)
			.where(conditions = [('id', '=', data['id'])]))
		#print(query.get())
		return self.run_query(query.get())

	def create(self, table_name = None):
		"""
		create(): It creates a new db record from passed data
		"""
		query = (self.build_query()
			.table(self.get_table_name() if table_name is None else table_name)
			.insert([self.get_attributes()])
			.get())
		return self.run_query(query)

	def destroy(self, conditions = '0'):
		"""
		destroy(): It removes records from db from the ids passed (ids must be a list)
		"""
		query = (self.build_query()
			.table(self.get_table_name())
			.delete()
			.where(conditions = conditions, glue = ' OR '))
		return self.run_query(query.get())

	def find(self, conditions = '1', fields = [], start_from = 0, limit = 18446744073709551615, join = [], order_by = 'created_at DESC'):
		"""
		find(): It finds records with the specified fields according the referred limits
		"""
		raw_fields = []
		for model_name, reference in join:
			raw_fields += list("{} AS {}_{}".format(field if '.' in field else '{}.{}'.format(self.model(name = model_name).get_table_name(), field), model_name.lower(), field) for field in self.model(name = model_name).get_fields())
		
		query = (self.build_query()
			.table(self.get_table_name())
			.select(fields = fields if len(fields) > 0 else self.get_fields(), raw_fields = raw_fields, start = start_from, limit = limit))

		for model_name, reference in join:
			join_table = self.model(name = model_name).get_table_name()
			query.join(table_name = join_table, conditions = [(reference if '.' in reference else "{}.{}".format(self.get_table_name(), reference), '=', '{}.{}'.format(join_table, 'id'))])

		query.where(conditions = conditions, glue = ' AND ').orderBy(order_by)

		#print(query.get())

		return self.run_query(query.get())