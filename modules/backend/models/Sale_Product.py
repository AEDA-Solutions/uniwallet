from framework import Model as std

class Sale_Product(std.Model):
	attributes = ['sale_id', 'product_id', 'quantity']
	table_name = "Sale_Product"