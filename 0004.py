'''
0004/0025
任一个英文的纯文本文件
统计其中的单词出现的个数
'''
import collections
import re

def replace(s):
    if s.group(1) == 'n\'t':
        return s.group(1)
    return ' '

def count_words(file):
    try:
        with open(file, 'r') as f:
            dic = collections.defaultdict(lambda:0)
            data = f.read().lower()
            data = re.sub(r'(n[\']t)|([\W\d])', replace, data)
            datalist = re.split(r'[\s\n]+', data)
            for item in datalist:
                dic[item] += 1
            del dic['']
            return dic
    except:
        print('file open error!')

if __name__ == "__main__":
    try:
        dic = count_words('words.txt')
        for key, val in dic.items():
            print(key, '--', val)
    except:
        print('no input file')
            