from framework import Model as std

class Purchase_Product(std.Model):
	attributes = ['purchase_id', 'product_id', 'quantity']
	table_name = "Purchase_Product"