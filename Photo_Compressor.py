from tkinter.filedialog import *
from PIL import Image

file_loc=askopenfilenames()

img = Image.open(file_loc[0])
img = img.convert('RGB')
img.save("Compressed.jpg", "JPEG", optimize = True, quality = 50)
print("Image is Compressed")