import hashlib

def make_hash(str_input):
	return hashlib.sha256(str_input.encode('utf-8')).hexdigest()