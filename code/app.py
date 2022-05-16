import pytesseract
import fitz
import pytesseract
from os import walk
from time import sleep

"""for page in doc.pages(start, stop, step):
# do something with 'page'
""" 

pdf = open('/home/galantini/Documents/proyects/write-out-images/source/FCE FIPUB Dimension 04 2021.pdf')
open_pdf = fitz.open(pdf)

print('In your pdf, identify the pages to be read and put the first and the last.')
start_page=input('First page:\n')
stop_page=input('Last page:\n')

num_of_pages=stop_page - start_page + 1


#CREATE IMAGES
for i in range(num_of_pages):
    pdf_page = start_page+i
    actPage = open_pdf[pdf_page-1]

    pix = actPage.get_pixmap(dpi=300)
    pix.save(f"/home/galantini/Documents/proyects/write-out-images/images/page{pdf_page}-save.png")
pdf.close()

print('sleep 10 sec')
sleep(10)


#READ IMAGE AND STORE IT
filedir = r"/home/galantini/Documents/proyects/write-out-images/images/"
for root, dirs, filename in walk(filedir, topdown=False):
    for numPages in range(len(filename)):
        pdf_page = start_page+numPages
        print(f'--------------Page {pdf_page}--------------')
        pImage= pytesseract.image_to_string(f'/home/galantini/Documents/proyects/write-out-images/images/page{pdf_page}-save.png',lang='spa')
        writeFile = open('/home/galantini/Documents/proyects/write-out-images/source/FCE-FIPUB-Dimension-04-2021','a')
        writeFile.write(f'\n--------------Page {pdf_page}--------------\n')
        writeFile.write(pImage)
        writeFile.close()