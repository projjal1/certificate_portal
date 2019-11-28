from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

usr=input()
event=input()
l=len(usr)
x=0
if(l>=14):
    x=l-14
    x=x/2
else:
    pass

start=485-x*20

img = Image.open("out.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("arial.ttf",50)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((start,340),usr,fill='black',font=font)
font = ImageFont.truetype("arial.ttf",25)
draw.text((530,465),event,fill='black',font=font)

img.save('sample-out.jpg')