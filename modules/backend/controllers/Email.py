import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
class Email:
	def send(self):
		body = str(self)

		fromaddr = "suporte.uniwallet@gmail.com"
		toaddr = "suporte.uniwallet@gmail.com"
		msg = MIMEMultipart()
		msg['From'] = "Suporte"
		msg['To'] = toaddr
		msg['Subject'] = "Atendimento"
 
		msg.attach(MIMEText(body, 'plain'))
 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "Uni123456")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		return "beuleza"
data = {'ddddddd'}
Email.send(data)