'''
0005/0025
你有一个目录
装了很多照片
把它们的尺寸变成都不大于 iPhone5 分辨率的大小
'''
from PIL import Image
import os

def reSize(filename, match_size):
    image = Image.open(filename)
    w, h = image.size
    mwidth, mheight = match_size[0], match_size[1]
    if w <= mwidth and h <= mheight:
        print(filename, 'match with iphone5.')
        return 
    if 1.0*w/mwidth > 1.0*h/mheight:
        scale = 1.0*w/mwidth
        new_im = image.resize((int(w/scale), int(h/scale)), Image.ANTIALIAS)
    else:
        scale = 1.0*h/mheight
        new_im = image.resize((int(w/scale), int(h/scale)), Image.ANTIALIAS)
    new_im.save('new-'+filename)
    new_im.close()

if __name__ == "__main__":
    ext = ['jpg', 'jpeg', 'png']
    match_size = [640, 1130]
    # 获得当前路径文件列表
    files = os.listdir(os.getcwd())

    for file in files:
        '''
        str.split(str="",num=string.count(str))[n]
        str:表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
        num:表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量
        [n]:表示选取第n个分片
        '''
        if file.split('.')[-1] in ext:
            reSize(file, match_size)

