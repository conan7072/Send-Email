import smtplib, ssl

class Send_Email():
    def __init__(self,sender,password,receiver):
        self.user_name=sender
        self.password=password
        self.port = 587  # For starttls
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = sender
        self.receiver_email = receiver

    def send(self,message):
        message = message
        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(self.user_name, self.password)
            server.sendmail(self.sender_email, self.receiver_email, message)


if __name__ == '__main__':
    Email=Send_Email('mrtknecht@gmail.com','Qwerty123!?','mrtknecht@gmail.com')
    Email.send('This is a try')