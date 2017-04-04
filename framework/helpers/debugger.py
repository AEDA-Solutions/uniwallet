import os

def applog(line, file_name = "general.log"):
	with open("log/{}".format(file_name), 'a') as file:
		file.write("{}\n".format(line))

def resetlog(file_name = "general.log"):
	os.remove("log/{}".format(file_name))