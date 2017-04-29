import json

def decode_JSON(content):
	"""
	decode_JSON(): It returns a dict from the JSON string input. If there is error on JSON format, it retuns a empty dict
	"""
	try:
		decoded_content = json.loads(content)
	except (ValueError):
		decoded_content = {}
	return decoded_content

def encode_JSON(content):
	"""
	encode_JSON(): It packs the content in JSON format
	"""
	try:
		encoded_content = json.dumps(content)
	except (ValueError):
		encoded_content = json.dumps({})
	return encoded_content