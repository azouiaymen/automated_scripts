from fpdf import FPDF

Pdf = FPDF()

list_of_images = ["ttt.jpg"]

for i in list_of_images: # list of images with filename
    Pdf.add_page()
    Pdf.image(i,0,0,255,255)

Pdf.output("yourfile.pdf", "F")