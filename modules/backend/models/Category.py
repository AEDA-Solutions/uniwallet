from framework import Model as std

class Company(std.Model):
	
	attributes = ['company_id', 'name', 'description']
	table_name = "Categories"