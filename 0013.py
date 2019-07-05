'''
0013/0025
用 Python 写一个爬图片的程序
'''
import os
import re
import urllib.request

def pic_collector(url, path):
    content = urllib.request.urlopen(url).read()
    r = re.compile(r'<img class="BDE_Image".*?src="(.*?)".*?>')
    pic_list = r.findall(content.decode('utf-8'))

    os.chdir(path)
    for i in range(len(pic_list)):
        pic_num = str(i) + '.jpg'
        urllib.request.urlretrieve(pic_list[i], pic_num)
        print("success!" + pic_list[i])

if __name__ == "__main__":
    url = "http://tieba.baidu.com/p/5969777821"
    path = "/Users/apple/Documents/图片/Yumi"
    pic_collector(url, path)





    