'''
0008/0025
一个HTML文件
找出里面的正文
'''
from bs4 import BeautifulSoup
import requests

def search_body(path):
    page = requests.get(path)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(str(page.text), 'html.parser')
    article = soup.find_all('body')
    print(article)

if __name__ == "__main__":
    Path = 'https://www.runoob.com/python/python-tutorial.html'
    search_body(Path)

