from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import xlrd 



from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Adding custom fonts. 1st parm is the name of the font and 2nd is the path to the ttf font file.
pdfmetrics.registerFont(TTFont('Roboto', 'RobotoMono-Medium.ttf'))
pdfmetrics.registerFont(TTFont('RobotoL', 'RobotoMono-Light.ttf'))

#packet = io.BytesIO()
# Function to return a pdf page with the parameters added into it.
def createpage(name):
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    
    
    #can.setFont('Roboto', 70)                # Setting the font and size of text.
    #can.drawString(300, 925, name)           # Drawing a string onto the page. (x, y, string)

    #can.setFont('RobotoL', 48)
    #can.drawString(160, 290, name)
    #can.drawString(2110, 785, seat)
    #can.drawString(2110, 648, food.upper())
    
    #if cusat=="cusat":
     #   can.drawString(2110,510,"CUSAT")

    #can.drawInlineImage("image.jpg",1560,270,)

    #can.setFont('RobotoL', 60)
    #can.drawString(1600, 648, seat)

    # =======================================================================================================
    # Code to centre a string between a starting and ending coordinates.

    can.setFillColorRGB(255, 0, 0)
    can.setFont('Roboto', 38)

    # You'll have to determine the following values with the help of the helper file, get_pdf_coordinates.py
    start = 0
    end = 840
    width_of_one_letter = 23           # Use some 'monospaced' font so that each letter will have the same length.
    y = 305

    mid = start + (end-start)/2
    #can.drawString(mid,y,"a")
    half_string_size = (len(name)/2)*width_of_one_letter
    #print(half_string_size*2)
    x = mid - half_string_size
    can.drawString(x, y, name)
    # =======================================================================================================
    

    can.save()                               # Save the canvas


    packet.seek(0)
    # Creating a pdf with just the canvas we just created.
    new_pdf = PdfFileReader(packet)

    # Read your existing PDF (ticket.pdf)
   
    existing_pdf = PdfFileReader(open("certificate2.pdf", "rb"))
    #else:
     # existing_pdf = PdfFileReader(open("nonveg.pdf", "rb"))
    # Add the canvas on the existing page
    page = existing_pdf.getPage(0)
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)

    return page


   
    #output = PdfFileWriter()

    
  
    #for i in range(sheet.nrows): 
    #  print(sheet.cell_value(i, 2)) 
    

      
    #output.addPage(page)                 # Adding that page to the pdf.
    
      # Writing it to a file.
    #outputStream = open("certificatenew.pdf", "wb")
    #output.write(outputStream)
    #outputStream.close()

def createpdf():
    print("sghfh")

if __name__=="__main__":
    
    createpage("KARTHYANI VENUGOPAL")
      



