from framework import Model as std
from helpers import dictionary

class Company(std.Model):
	
	attributes = ['user_id', 'name', 'cnpj']
	table_name = "Companies"