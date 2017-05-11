from framework import Model as std

class Company(std.Model):
	
	attributes = ['user_id', 'name', 'cnpj']
	table_name = "Companies"