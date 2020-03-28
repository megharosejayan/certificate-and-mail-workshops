import email, smtplib, ssl
import xlrd


from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





subject = "Tickets | TEDxCUSAT"
sender_email = "admin@tedxcusat.in"
password = ""
# password = input("Type your password and press enter:")


def mail(receiver_email, body):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = "TEDxCUSAT <admin@tedxcusat.in>"
    # message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = sender_email  # Recommended for mass emails (sending one email to multiple recepients) Not our case.

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtpout.asia.secureserver.net", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    print("hey")

if __name__ == "__main__":
    loc = ("details.xlsx") 
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 




    for i in range (78,101):

     
     receiver_email = sheet.cell_value(i,1)
     name = sheet.cell_value(i,2)
     print(name)
     body = "Dear " + name + "\n\nGreetings from TEDxCUSAT. If you haven't received your ticket yet, please do let us know.\n\n Regards,\n Megha Rose | TEDxCUSAT\n 9495884193"
    
     mail(receiver_email, body)
     mail("megharose15@gmail.com",body)

