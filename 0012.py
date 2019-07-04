'''
0012/0025
敏感词文本文件 filtered_words.txt
当用户输入敏感词语用星号 * 替换
例如当用户输入「北京是个好城市」变成「**是个好城市」
'''
import sys, os

filePath = os.path.join(sys.path[0],'filtered_words.txt')
inPath = os.path.join(sys.path[0],'inputfile.txt')
outPath = os.path.join(sys.path[0],'outputfile.txt')

wfilter = set()
with open(filePath) as f:
    for w in f.readlines():
        wfilter.add(w.strip())

with open(inPath) as targetf:
    count = len(targetf.readlines())
    i = 1
    for i in range(count):
        for w in wfilter:
            if w in targetf.readline(i):
                t = targetf.readline(i)
                t = t.replace(w,'*'*len(w))
                with open(outPath,'w') as outf:
                    outf.write(t)
                i = i + 1
