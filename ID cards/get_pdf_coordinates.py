from PyPDF2 import PdfFileWriter, PdfFileReader
import io

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Roboto', 'RobotoMono-Medium.ttf'))
pdfmetrics.registerFont(TTFont('RobotoL', 'RobotoMono-Light.ttf'))
# pdfmetrics.registerFont(TTFont('Robotomono', 'RobotoMono-Medium.ttf'))
packet = io.BytesIO()

# create a new PDF with Reportlab


def creatpdf(name, event):
    can = canvas.Canvas(packet)
    can.setFont('Roboto', 17)
    can.setFont('RobotoL', 24)
    can.drawString(35, 185, 'ROSE JAYAN')
    can.setFillColorRGB(255, 0, 0)
    can.setFont('Roboto', 24)
    can.drawString(35, 215, 'MEGHA')
    can.setFont('Roboto', 3)
    # can.setFont('Roboto', 70)

    
    # To find the font size.
    # for x in range(20):
    #     can.setFont('Roboto', x*5)
    #     can.drawString(x*20, 220, str(x*5))
    # can.save()

   # To find the x and y axes.
    for x in range(1000):
       can.drawString(x*10, 220, str(x*10)) # x axis
       can.drawString(40, x*10, str(x*10)) # y axis
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("idcard.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("certificate.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

if __name__ =="__main__":
    creatpdf("SAHIL", "MAKE-A-TON")
