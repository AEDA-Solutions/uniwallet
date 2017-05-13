import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
def send(fromemail, toemail, passw, content):
	body = str(content)

	fromaddr = str(fromemail)
	toaddr = str(toemail)
	msg = MIMEMultipart()
	msg['From'] = "Suporte"
	msg['To'] = str(toaddr)
	msg['Subject'] = "Atendimento"

	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(str(fromaddr), str(passw))
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()



	