"""
Under construction by Uniwallet team
This class will make all SQL queries for our application
"""

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

		def select(self, fields = []):
			return (QueryBuilder.Table.Select(self.table_name, fields))

		def insert(self):
			return (QueryBuilder.Table.Insert())

		def update(self):
			return (QueryBuilder.Table.Update())

		def delete(self):
			return (QueryBuilder.Table.Delete())

		class Common():

			def __init__(self, table):
				pass

			def where(self):
				pass

			def orderBy(self):
				pass

			def groupBy(self):
				pass

			def run(self):
				pass


		class Select(Common):

			def __init__(self, table_name, fields = []):
				self.table_name = table_name
				self.query = """
					SELECT
						
					{fields}

					FROM {table_name}

					[inner]

					[condition]
				""".format(fields = '*' if len(fields) is 0 else ", ".join(list("{}.{}".format(table_name, item) for item in fields)),
						   table_name = table_name)

			def join(self, table_name, conditions = []):
				snippet = """
					INNER JOIN

					{table_name}

					{conditions}
				"""
				self.query = self.query.replace('[inner]', snippet.format(table_name = table_name,
															 			  conditions = 'ON {}'.format(' '.join(list(item if isinstance(item, str) else '{}.{}{}{}.{}'.format(table_name, item[0], item[1], self.table_name, item[2]) for item in conditions)))))
				return self

		class Insert():

			def __init__(self, table):
				pass

		class Update(Common):

			def __init__(self, table):
				pass

		class Delete(Common):

			def __init__(self, table):
				pass


qb = QueryBuilder()
z = qb.table('Users')
print(z.select(['id', 'qwerty', 'fror', 'fude']).join("Marte", [['teste', '=', 'teste'], 'AND', ['User.teste', '=', 'umi.teste']]).query)
				
				
			
			