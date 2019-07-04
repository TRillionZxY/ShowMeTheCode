'''
0009/0025
一个HTML文件
找出里面的链接
'''
import requests
import pyquery

def search_url(url):
    url_list = []
    page = requests.get(url)
    doc = pyquery.PyQuery(page.content.decode())
    a_tags = doc.find('a')
    for a in a_tags.items():
        if a.attr('href').startswith('http'):
            url_list.append(a.attr('href'))
        elif a.attr('href').startswith('/'):
            url_list.append('https://github.com' + a.attr('href'))
    print(url_list)

if __name__ == "__main__":
    url = 'https://github.com/TRillionZxY'
    search_url(url)
