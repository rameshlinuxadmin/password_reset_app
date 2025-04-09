import smtplib
from email.message import EmailMessage
from cryptography.fernet import Fernet
import json


file =  open(".\config.json")
config = json.load(file) 

def mail(sender, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "<Mail ID>"
    smtp_password = "<App Password>"

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = sender

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        print("Email sent successfully")
        
    except Exception as e:
        print("Error", e)
def passwd_encrpt(passwd):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    #encrypted_passwd = Fernet(Fernet.generate_key()).encrypt(passwd.encode())
    encrypted_passwd = cipher_suite.encrypt(passwd.encode()) 
    return encrypted_passwd.decode() 

username = config["username"]
servername = config["servername"]
incident = config["incident"]
password = passwd_encrpt(config["password"])
subject = f"{incident}: Password reset request "
sender = "<Recipient Mail ID>"

body = f"{username} {servername} {password}"
mail(sender, subject, body)