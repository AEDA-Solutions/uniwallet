from framework import Model as std

class Store(std.Model):
	attributes = ['company_id', 'name']

	def find(self, fields = None, fields_to_ignore = [], start_from = 0, limit = 18446744073709551615, target_fields = ['*'], table_name = None):
		query = (self.build_query()
			.table(self.get_table_name() if table_name is None else table_name)
			.select(fields = self.attributes, start = start_from, limit = limit, raw_fields = ['Companies.id AS compid', 'Companies.name AS companame', 'Companies.cnpj AS cnpj'])
			.join('Companies', [['{}.company_id'.format(self.get_table_name()), '=', 'Companies.id']])
			.where(raw = '1' if fields is None else dictionary.implode(dictionary = dictionary.remove_fields(fields, fields_to_ignore), separator = '=', glue = ' AND '))
			.get())
		return self.run_query(query)