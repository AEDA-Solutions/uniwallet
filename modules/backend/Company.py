from framework import Model as std

class Company(std.Model):
	
	attributes = ['compname', 'email', 'location', 'password', 'phone', 'cnpj']
	table_name = "Companies"