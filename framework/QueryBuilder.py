"""
Under construction by Uniwallet team
This class will make all SQL queries for our application
"""
import re

class QueryBuilder:

	def __init__(self, transaction = False):
		"""
		TRANSACTION:https://dev.mysql.com/doc/refman/5.7/en/commit.html
		"""
		pass

	def table(self, name):
		return QueryBuilder.Table(name)

	class Table():
		def __init__(self, table_name):
			self.table_name = table_name

		def select(self, fields = [], start = 0, limit = 18446744073709551615, raw_fields = []):
			return (QueryBuilder.Table.Select(self.table_name, fields, start, limit, raw_fields))

		def insert(self, list_of_values_dict, ignore = False):
			return (QueryBuilder.Table.Insert(self.table_name, list_of_values_dict, ignore))

		def update(self, values_dict):
			return (QueryBuilder.Table.Update(self.table_name, values_dict))

		def delete(self):
			return (QueryBuilder.Table.Delete(self.table_name))

		class Common():

			query = None

			table_name = None

			def get(self):
				return re.sub(r'(\[.*\]|\t+)', '', self.query, flags=re.MULTILINE)

		class Filter(Common):

			def where(self, conditions = [], glue = '', raw = None):
				snippet = """
					WHERE

					{conditions}

					[condition]
				"""
				self.query = self.query.replace('[condition]', snippet.format(conditions = raw if raw is not None else "{}".format(glue).join( list(item if isinstance(item, str) else "{}.{}{}'{}'".format(self.table_name, item[0], item[1], item[2]) for item in conditions))))
				return self

		class Select(Filter):

			def __init__(self, table_name, fields, start, limit, raw_fields):
				self.table_name = table_name
				self.query = """
					SELECT
						
					{fields}

					FROM {table_name}

					[inner]

					[condition]

					LIMIT {start},{limit}
				""".format(fields = '*' if len(fields) is 0 else ", ".join(list("{}.{}".format(table_name, item) for item in fields) + raw_fields),
						   table_name = table_name,
						   start = start, 
						   limit = limit)

			def join(self, table_name, conditions = []):
				snippet = """
					INNER JOIN

					{table_name} AS {table_name}

					{conditions}

					[inner]
				"""
				self.query = self.query.replace('[inner]', snippet.format(table_name = table_name,
															 			  conditions = 'ON {}'.format(' '.join(list(item if isinstance(item, str) else '{}{}{}'.format(item[0], item[1], item[2]) for item in conditions)))))
				return self

			def orderBy(self, field):
				snippet = """
					ORDER BY

					{field}

					[condition]
				"""
				self.query = self.query.replace('[condition]', snippet.format(field = field))

				return self

			def groupBy(self, field):
				snippet = """
					GROUP BY

					{field}

					[condition]
				"""
				self.query = self.query.replace('[condition]', snippet.format(field = field))

				return self

		class Insert(Common):

			def __init__(self, table_name, list_of_values_dict, ignore):
				self.table_name = table_name
				fields = list_of_values_dict[0].keys()
				self.query = """
					INSERT{ignore}INTO

					{table_name}
						
					({fields})

					VALUES 

					{values}
				""".format(ignore = ' ' if ignore is False else ' IGNORE ',
						   table_name = table_name,
						   fields = (', '.join(list(item for item in fields))),
						   values = ('\n'.join(list(('({})'.format(', '.join(list("'{}'".format(values_dict[item]) for item in fields)))) for values_dict in list_of_values_dict))))

		class Update(Filter):

			def __init__(self, table_name, values_dict):
				self.table_name = table_name
				fields = values_dict.keys()
				self.query = """
					UPDATE 

					{table_name}
						
					SET

					{fields_values}

					[condition]
				""".format(table_name = table_name,
						   fields_values = (", ".join("{}.{}={}".format(self.table_name, item,  "'{}'".format(values_dict[item])) for item in fields)))

		class Delete(Filter):

			def __init__(self, table_name):
				self.table_name = table_name
				self.query = """
					DELETE FROM 

					{table_name}

					[condition]
				""".format(table_name = self.table_name)