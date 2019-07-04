'''
0006/0025
你有一个目录放了你一个月的日记(txt)
为了避免分词的问题
假设内容都是英文
请统计出你认为每篇日记最重要的词
'''
import collections
import re
import string
import os

def get_word(filename):
    '''
    从一个txt文件中找出出现次数最高的词及其对应次数，以元组形式返回
    '''
    stop_word = ['the', 'in', 'of', 'and', 'to', 'has', 
    'that', 'this','s', 'is', 'are', 'a', 'with', 'as', 'an']

    f = open(filename, 'r')
    content = f.read().lower()
    pat = '[a-z0-9\']+'
    words = re.findall(pat, content)
    wordList = collections.Counter(words)
    for i in stop_word:
	    wordList[i] = 0
    f.close()
    return wordList.most_common()[0]

def traverseFile (path):
    '''
    遍历路径文件夹中的所有文件，并调用get_word函数，输出统计结果
    '''
    for file in os.listdir(path):
        if file.split('.')[-1] in 'txt':
            #调用get_word函数
            most_important = get_word(file)
            print(most_important[0] + ' is the most important word in the essay:' + file)
            print('the using times of ' + most_important[0] + "is:" + repr(most_important[1]))
            print("")

if __name__ == "__main__":
    traverseFile(os.getcwd())