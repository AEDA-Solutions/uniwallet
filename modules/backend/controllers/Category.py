from . import Controller as std

class Category(std.Controller):
	def fetchadmin(self):
		mask = self.metadata([('id', ':::hide'), ('type', ':Tipo')])
		return (self.model().find(start_from = self.get_input('start'), limit = self.get_input('limit'))
			.fetch(fields_mask = mask))

	def select(self):
		return self.model().find().fetch(fields_mask = [('id', 'value'), ('type', 'content')])

	def register(self):
		count = self.model(data = self.get_request_parameters()).save().count_rows()
		return "Done: Category created {} rows affected".format(count)

	def update(self):
		count = self.model(data = self.get_request_parameters()).save().count_rows()
		return "Done: Category updated {} rows affected".format(count)