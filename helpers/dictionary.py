def remove_fields(dictionary, list_fields):
	"""
	remove_fields(): It filters a dictionary return the passed dictionary without the referred keys
	"""
	for field in list_fields:
		if field in dictionary.keys():
			del dictionary[field]
	return dictionary

def select(dictionary, list_fields):
	"""
	select(): It filters a dictionary return the passed dictionary just with the referred keys
	"""
	filtered = []
	for key, value in dictionary.items():
		if key in list_fields:
			filtered.append(tuple([key, value]))
	return dict(filtered)

def mask(dictionary, tuple_list_fields):
	"""
	mask(): It filters a dictionary return the passed dictionary and it renames the dict keys according the tuple passed
	"""
	filtered = []
	for key, mask in tuple_list_fields:
		if key in dictionary:
			filtered.append(tuple([mask, dictionary[key]]))
	return dict(filtered)

def alias(dictionary, tuple_list_fields):
	"""
	alias(): It give aliases to the dict keys
	"""
	filtered = []
	aliases = dict(tuple_list_fields)
	for key, value in dictionary.items():
		if key in aliases:
			filtered.append(tuple([aliases[key], value]))
		else:
			filtered.append(tuple([key, value]))
	return dict(filtered)

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
