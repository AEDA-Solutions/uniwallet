from framework.Controller import Controller

class General(Controller):

	def controllernotfound(self):
		return self.forbid("Controller '{}' from module '{}' not found".format(self.request.controller, self.request.module), 'Not Found')

	def actionnotfound(self):
		return self.forbid("Action '{}' unavailable".format(self.request.action), 'Not Found')
