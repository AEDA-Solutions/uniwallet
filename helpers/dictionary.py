def remove_fields(dictionary, list_fields):
	"""
	remove_fields(): It filters a dictionary return the passed dictionary without the referred keys
	"""
	for field in list_fields:
		if field in dictionary.keys():
			del dictionary[field]
	return dictionary

def implode(dictionary, separator, glue=', ', key_prefix='', value_prefix=''):
	"""
	implode(): It brings together the dict elements into a string and it separates each element with 'glue' attribute
	"""
	list_elem = list("{}{}{}{}{}".format(key_prefix, key, separator, value_prefix, elem) for key, elem in dictionary.items())
	return glue.join(list_elem)

def quote_values(dictionary):
	return dict( (key, "'{}'".format(elem)) for key, elem in dictionary.items() )
