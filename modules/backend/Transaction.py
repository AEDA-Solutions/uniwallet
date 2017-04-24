from framework import Model as std

class Transaction(std.Model):

	attributes = ['operation', 'value']
	#table_name = 'Transaction'