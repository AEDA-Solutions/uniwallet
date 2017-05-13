from framework import Session as std

class Sale(std.Transaction):
	pass

	#The buyer (user_id) is represented as the 'from' Transaction attribute
	#The seller (store_id) is represented as the 'to' Transaction attribute