from framework import Controller as std

class Controller(std.Controller):
	def metadata(self, tuple_list):
		"""
		metadata(): It appends metadata to the list passed in order to format output for datables
		"""
		fields = []
		for item in tuple_list:
			pieces = item[1].split(':')
			if len(pieces[0]) > 0:
				label = item[1]
			else:
				label = "{}{}".format(item[0], item[1])
			fields.append(tuple([item[0], "{}".format(label)]))
		return fields