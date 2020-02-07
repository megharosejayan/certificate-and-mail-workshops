from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import xlrd 
from qr import qrfun


from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Adding custom fonts. 1st parm is the name of the font and 2nd is the path to the ttf font file.
pdfmetrics.registerFont(TTFont('Roboto', 'RobotoMono-Medium.ttf'))
pdfmetrics.registerFont(TTFont('RobotoL', 'RobotoMono-Light.ttf'))

#packet = io.BytesIO()
# Function to return a pdf page with the parameters added into it.
def createpage(fname, lname, image):
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    


    can.setFont('RobotoL', 24)
    can.drawString(35, 180, lname.upper())

    can.setFillColorRGB(255, 0, 0)
    can.setFont('Roboto', 24)
    can.drawString(35, 210, fname.upper())

    can.drawInlineImage("image.jpg",35,120)

    can.save()                               # Save the canvas


    packet.seek(0)
    # Creating a pdf with just the canvas we just created.
    new_pdf = PdfFileReader(packet)

    # Read your existing PDF (ticket.pdf)
    existing_pdf = PdfFileReader(open("idcard.pdf", "rb"))
    # Add the canvas on the existing page
    page = existing_pdf.getPage(0)
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)

    return page



def createpdf():
    image = qrfun('ibQiUCvz0fcy6dcZxNEV')
    page = createpage('Remya', 'Ramachandran', image)
    output = PdfFileWriter()

    output.addPage(page)                 # Adding that page to the pdf.
    
      # Writing it to a file.
    outputStream = open("TEDxCUSAT Ticket.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

if __name__=="__main__":
    createpdf()



