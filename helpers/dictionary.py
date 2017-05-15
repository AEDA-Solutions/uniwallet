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

def tuplefy(dictionary, glue = None):
	tuple_list = []
	for item in dictionary.items():
		tuple_list.append(item if glue is None else tuple([item[0], glue, item[1]]))
	return tuple_list

def access_nested_elem_from_list(dicT, lisT):
	for item in lisT:
		try:
			dicT = dicT[item]
		except:
			return None
	return dicT
