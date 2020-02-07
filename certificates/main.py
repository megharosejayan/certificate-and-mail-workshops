import xlrd 
from PyPDF2 import PdfFileWriter, PdfFileReader

from create_certificate import createpage



loc = ("details.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 


output = PdfFileWriter()

#for i in range (1,101):

#name=sheet.cell_value(i,2)
        #calling function to generate qr code. Return the QR code image 

page = createpage("Mr.TEEKA RAM MEENA IAS")   #calling function to create pdf
output.addPage(page)  
page = createpage("Mr.SUDEV NAIR") 
output.addPage(page)  
page = createpage("Mr.NITIN VASANTH")
output.addPage(page)   
page = createpage("Dr.M.R.RAJAGOPAL")
output.addPage(page)   
page = createpage("Mr.BINOAY B") 
output.addPage(page)  
page = createpage("Mr.ANTO PHILIP") 
output.addPage(page)  
page = createpage("Dr.VINEETH PALERI") 
output.addPage(page)                 # Adding that page to the pdf.



# Writing it to a file.
outputStream = open("TEDxCUSAT Speakers certificates.pdf", "wb")
output.write(outputStream)
outputStream.close()
