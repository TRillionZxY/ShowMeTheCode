'''
0011/0025
敏感词文本文件filtered_words.txt
当用户输入敏感词语时打印出Freedom
否则打印出Human Rights
'''
import sys, os

filePath = os.path.join(sys.path[0],'filtered_words.txt')
wfilter = set()
with open(filePath) as f:
    for w in f.readlines():
        wfilter.add(w.strip())
        
while True:
    s = input()
    if s in wfilter:
        print('Freedom')
    else:
        print('Human Right')
    if s == 'exit':
        break
        
