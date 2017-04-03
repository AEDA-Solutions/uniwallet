from framework import Connection as std
from app.db import config as db

class Model:
	def __init__(self):
		self.db = std.Connection(db.config())
		