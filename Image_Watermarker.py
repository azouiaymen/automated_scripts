from PIL import Image, ImageDraw, ImageFont

img = Image.open(r'./ttt.jpg') 

draw = ImageDraw.Draw(img) 

text = "subscribe"
font = ImageFont.truetype('arial.ttf', 82)


textwidth, textheight = draw.textsize(text, font)
width, height = img.size 
x=width/2-textwidth/2
y=height-textheight-300


draw.text((x, y), text, font=font) 

img.save(r'watermaked.png')