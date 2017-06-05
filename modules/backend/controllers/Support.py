from framework import Controller as std
from helpers.email import send

class Support(std.Controller):
	
	def report(self):
		messagem = "nome: {}\nemail\n{}\nconteúdo:{}".format(self.get_input("name"), self.get_input("email"), self.get_input("content"))
		send(fromemail = "suporte.uniwallet@gmail.com", toemail = "suporte.uniwallet@gmail.com", passw = "Uni123456", content = messagem)
		return messagem

	def baz(self):
		return self.view('General').format("Hello")

	def mulheres(self):
		return "Este conteúdo está aqui no backend"

	def dados(self):
		return {
			"nome": "Caio Silva",
			"idade": 29
		}