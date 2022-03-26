import smtplib
from email.message import EmailMessage
import imghdr
import codecs
import os

def enviarMail(mail):
    print("Starting to send the email.")

    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Your QR has arrived!" 
    newMessage['From'] = 'yourMail@mail.com'                  
    newMessage['To'] = mail                 
    newMessage.set_content('Let me know what you think. Image attached!') 

    with open('imagen.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    #msg_full = message.as_string()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('yourMail@mail.com', 'yourPassword')
    server.sendmail('yourMail@mail.com',
                    mail,
                    newMessage.as_string())
    os.remove("imagen.png")
    print("Finished sending email")
