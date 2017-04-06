from framework import Middleware as std

class Test(std.Middleware):
	def coisa(self, request):
		return self.rules({
				"fields": {
					"name": ["required"],
					"teste": "required"
				},
				"auth": ["manager", "client"]
			}, request)

