from . import Controller as std

class University(std.Controller):
	def fetchadmin(self):
		mask = self.metadata([('id', ':::hide'), ('name', ':Nome'), ('abbreviation', ':Sigla')])
		return (self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))

	def select(self):
		return self.model().find().fetch(fields_mask = [('id', 'value'), ('name', 'content')])

	def register(self):
		count = self.model(data = self.get_request_parameters()).save().count_rows()
		return "Done: University created {} rows affected".format(count)

	def update(self):
		count = self.model(data = self.get_request_parameters()).save().count_rows()
		return "Done: University updated {} rows affected".format(count)