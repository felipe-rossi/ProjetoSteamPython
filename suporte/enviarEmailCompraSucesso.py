import smtplib

def enviarEmailCompra():
    servidor_email = smtplib.SMTP("smtp.gmail.com", 587)
    servidor_email.starttls()
    servidor_email.login('felipaovs12@gmail.com','akdr htio emuw zgyq')

    remetente = 'felipaovs12@gmail.com'
    destinatarios = ['felipaovs12@gmail.com']
    conteudo = "Faca com valor menor que 100 reais foi comprada!!!"

    servidor_email.sendmail(remetente, destinatarios, conteudo)

    servidor_email.quit()