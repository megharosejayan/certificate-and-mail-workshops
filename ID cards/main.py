
import xlrd 
from PyPDF2 import PdfFileWriter, PdfFileReader

from create_certificate import createpage
from qr import qrfun


loc = ("details.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 


output = PdfFileWriter()

for i in range (1,101):

    name=sheet.cell_value(i,4)
    idno=sheet.cell_value(i,8)   #idno is a unique id which will be showed when the qr code is scanned
    # print(name)
    lname = ''
    if name == 'custom':
        fname = sheet.cell_value(i,2)
        lname = sheet.cell_value(i,3)
    else:
        fname = name.split(' ')[0]
        if(len(name.split(' ')) > 1):
            lname = name.split(' ')[1]

    print(fname)
    print(lname)
    print(idno)
    print('\n')
    image = qrfun(idno)         #calling function to generate qr code. Return the QR code image 

    page = createpage(fname,lname,image)   #calling function to create pdf
    output.addPage(page)                 # Adding that page to the pdf.



# Writing it to a file.
outputStream = open("TEDxCUSAT ID cards.pdf", "wb")
output.write(outputStream)
outputStream.close()
