import pkgutil
import importlib

def fit_pair_to_list(pair_list, new_pair):
	new_pair_list = []
	for pair in pair_list:
		if new_pair and pair[0] == new_pair[0]:
			new_pair_list.append(new_pair)
			new_pair = None
		else:
			new_pair_list.append(pair)
	if new_pair:
		new_pair_list.append(new_pair)
	return new_pair_list

def get_package_modules(package):
	modules_list = []
	for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
		if not ispkg:
			modules_list.append(modname)
	return modules_list

def get_package_from_module(self, package_name, module_name):
		"""
		get_package_from_module(): It gets an package from the modules module
		"""
		try:
			mod = importlib.import_module("modules.{}.{}".format(module_name, package_name))
		except Exception:
			mod = None
		return mod

def get_package_from_module(package_name, module_name):
	"""
	get_package_from_module(): It gets an package from the modules module
	"""
	try:
		mod = importlib.import_module("{}.{}".format(module_name, package_name))
	except Exception:
		mod = None
	return mod

def replace_on_list(list_, target, replace_by):
	for pos, content in enumerate(list_):
		list_[pos] = list_[pos].replace(target, replace_by)
	return list_


