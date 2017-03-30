def dump_env(env):
	output = ""
	for key, value in env.items():
		output += "{}: {}<br />".format(key, value)
	return output