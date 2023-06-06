from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def func(input_file, output_file, name, sname, address, postcode, city, country, gender, height):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(128, 460, name)
    can.drawString(128, 438, sname)
    can.drawString(128, 417, address)
    can.drawString(128, 396, postcode)
    can.drawString(128, 375, city)
    can.drawString(128, 353, country)
    can.drawString(128, 332, gender)
    can.drawString(128, 311, height)
    can.save()

    packet.seek(0)

    new_pdf = PdfFileReader(packet)

    existing_pdf = PdfFileReader(open(input_file, "rb"))
    output = PdfFileWriter()

    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    output_stream = open(output_file, "wb")
    output.write(output_stream)
    output_stream.close()


# Provide the input PDF file name, output PDF file name, and the name to be added
input_file = "Motor.pdf"
output_file = "New.pdf"
name = "Rohan"
sname= "Kant"
address= "XXX 19th Floor,Challengers Housing Society,Thakur Village"
postcode="400101"
city="Mumbai"
country="India"
gender="Male"
height="178cm"
func(input_file, output_file, name, sname, address, postcode, city, country, gender, height)