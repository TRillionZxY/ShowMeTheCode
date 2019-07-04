'''
0010/0025
使用 Python 生成类似于下图中的字母验证码图片
'''
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys, os
import random

savePath = os.path.join(sys.path[0],'photokey.jpg')

def randChar():
    return chr(random.randint(65, 90))

def randColor():
    return (random.randint(64, 255), 
            random.randint(64, 255), 
            random.randint(64, 255))
    
def randColor2():
    return (random.randint(32, 127), 
            random.randint(32, 127), 
            random.randint(32, 127))
    
def get_photokey(width,height,count):
    image = Image.new('RGB', (width, height), (255,255,255))
    font = ImageFont.truetype('Arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    
    for x in range(width):
        for y in range(height):
            draw.point((x,y), fill=randColor())
            
    for t in range(count):
        draw.text((height*t + 10, 10), randChar(), font=font, fill=randColor2())
        
    image = image.filter(ImageFilter.BLUR)
    image.save(savePath, 'jpeg')
    
if __name__ == '__main__':
    count = 4
    width = 60*count
    height = 60
    get_photokey(width,height,count)
