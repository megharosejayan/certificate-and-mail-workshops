import email, smtplib, ssl
import xlrd


from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





subject = "TEDxCUSAT"
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




    for i in range (1,101):

     
     receiver_email = sheet.cell_value(i,1)
     name = sheet.cell_value(i,2)
     
     body = "Dear " + name + "\n\nGreetings from TEDxCUSAT.\nAs the first-ever edition of TEDxCUSAT wraps up, we wanted to thank you from the bottom of our hearts, for having been an immensely important part of this wonderful journey that TEDxCUSAT has been. We are grateful to you for having been part of the amazing audience that was co-operative and  enthusiastic throughout the event. We are extremely sorry for any kind of inconvenience caused by us, including the technical glitch in the start of the event. It was our honor to host you here at CUSAT and we hope that you enjoyed attending TEDxCUSAT.  We hope to meet you real soon!\n\nBest wishes and regards,\nTEDxCUSAT Team"
     
     print("hello")
     print(name)
     mail(receiver_email, body)
     #mail("megharose15@gmail.com",body)
     print("over")

