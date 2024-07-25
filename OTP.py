import random
import smtplib
from email.message  import EmailMessage

otp=""
for i in range(6):
    otp += str(random.randint(0,9))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

from_mail = '[Your Gmail]' #Gmail account
server.login(from_mail,'[App Password]') #App password from your google account
to_email = input("Enter Your Email: ")
print("Email Sended")

msg= EmailMessage()
msg['Subject'] = "OTP Verification"
msg['From'] = from_mail
msg['To'] = to_email
msg.set_content("Your OTP is: "+otp)

server.send_message(msg)

input_otp = input("Enter the OTP: ")
if input_otp == otp:
    print("OTP Verified")
else:
    print("OTP Invalid")