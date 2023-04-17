import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587 )
server.starttls()

def send_mail( details ):
    sender_email = 'artibot.artimas@gmail.com'
    server.login(sender_email, 'cqjuhccwupsfhfkd')

    server.sendmail(sender_email, details[2], f'Subject: {details[3]} - Mail by {details[1]} using artibot chatbot' + '\n' + details[4] + '\n\n\nThis message was sent using artibot chatbot.' )