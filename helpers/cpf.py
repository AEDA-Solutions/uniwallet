"""
function created according the rules described on http://www.geradorcpf.com/algoritmo_do_cpf.htm
"""
import re
def is_cpf_valid(raw_cpf):
	"""
	cpf_is_valid(): It receives a cpf and return True if it's valid or False otherwise
	"""
	cpf = raw_cpf.replace('.', '').replace('-', '') #It removes dots and hyphens
	cpf_pattern = re.compile("^[0-9]{11}$") #It defines that the string must contais 11 number characters
	if cpf_pattern.match(cpf):
		first_check_digit = fetch_check_digit(cpf[0:9]) 
		second_check_digit = fetch_check_digit("{}{}".format(cpf[0:9], first_check_digit))
		return cpf == "{}{}{}".format(cpf[0:9], first_check_digit, second_check_digit)
	else:
		return False

def fetch_check_digit(snippet):
	"""
	fetch_check_digit(): It returns a check digit from a input according the rules source (Check url)
	"""
	product = 0
	for algarism in range(len(snippet) + 1, 1, -1):
		product = product + int(snippet[len(snippet) - algarism + 1]) * algarism
	rest = product % 11
	if rest < 2:
		return 0
	else:
		return 11 - rest



		