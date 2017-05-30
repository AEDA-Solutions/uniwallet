from framework import Model as std
from helpers import dictionary

class Transaction(std.Model):
	attributes = ['destiny', 'operation', 'value']