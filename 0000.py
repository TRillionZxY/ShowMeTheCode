'''
0000/0025
将你的 QQ 头像（或者微博头像）右上角加上红色的数字
类似于微信未读信息数量那种提示效果
'''
from PIL import Image, ImageDraw, ImageFont

image = Image.open('0.jpg')
w, h = image.size
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Arial.ttf',size=128)

draw.ellipse((5*w/6, 0, w, h/6),fill=(255,0,0))
draw.text((5*w/6, h/30), '10', fill=(255,255,255), font=font)
image.save('0.1.png', 'png')