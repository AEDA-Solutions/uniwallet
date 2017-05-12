from framework import Model as std

class Company(std.Model):
	
	attributes = ['user_id', 'name', 'cnpj']
	table_name = "Companies"

	def find(self, fields = None, fields_to_ignore = None, start_from = 0, limit = 18446744073709551615, target_fields = ['*'], table_name = None):
		query = (self.build_query()
			.table(self.get_table_name() if table_name is None else table_name)
			.select(start = start_from, limit = limit)
			.join('Users', [['Companies.user_id', '=', 'Users.id']])
			.where(raw = '{fields} AND {to_ignore}'.format(
					fields = 1 if fields is None or len(fields) == 0 else " OR ".join(list((1 if item is None else " AND ".join(list("{}={}{}{}".format(elem, "'", item[elem], "'") for elem in item))) for item in fields)),
					to_ignore = 1 if fields_to_ignore is None or len(fields_to_ignore) == 0 else " OR ".join(list((1 if item is None else " AND ".join(list("{}<>{}{}{}".format(elem, "'", item[elem], "'") for elem in item))) for item in fields_to_ignore))))
			.get())
		return self.run_query(query)