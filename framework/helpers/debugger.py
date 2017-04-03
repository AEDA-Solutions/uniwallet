import os

def applog(line, file_name = "debug.log"):
	with open(file_name, 'a') as file:
		file.write("{}\n".format(line))

def resetlog(file_name = "debug.log"):
	os.remove(file_name)