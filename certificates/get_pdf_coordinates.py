from PyPDF2 import PdfFileWriter, PdfFileReader
import io

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Roboto', 'RobotoMono-Medium.ttf'))
pdfmetrics.registerFont(TTFont('Robotomono', 'RobotoMono-Medium.ttf'))
packet = io.BytesIO()

# create a new PDF with Reportlab


def creatpdf(name, event):
    can = canvas.Canvas(packet)
    # can.setFont('Roboto', 5)
    # can.setFont('Roboto', 70)

    
    # To find the font size.
    for x in range(20, 50, 2):
        can.setFont('Roboto', x)
        can.drawString((x-30)*40, 295, str(x))
    # can.save()

    can.setFillColorRGB(255, 0, 0)
    can.setFont('Roboto', 38)

    # You'll have to determine the following values with the help of the helper file, get_pdf_coordinates.py
    start = 5
    end = 600
    width_of_one_letter = 18            # Use some 'monospaced' font so that each letter will have the same length.
    y = 295

    mid = start + (end - start)/2
    half_string_size = (len(name)/2)*width_of_one_letter
    print(half_string_size*2)
    x = mid - half_string_size
    can.drawString(x, y, name)

    can.setFont('Roboto', 1)

    

   # To find the x and y axes.
    for x in range(1000):
       can.drawString(x*3, 294, str(x*3)) # x axis
       can.drawString(140, x*3, str(x*3)) # y axis
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("certificate1.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("certificatenew.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

if __name__ =="__main__":
    creatpdf("REMYA RAMACHANDRAN", "MAKE-A-TON")
