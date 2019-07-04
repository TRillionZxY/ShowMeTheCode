'''
0007/0025
有个目录里面是你自己写过的程序
统计一下你写过多少行代码-空行-注释
分别列出来
'''
import os
import re

code_lines = []
note_lines = []
blank_lines = []

def findfile(filename):
    global code_lines
    global note_lines
    global blank_lines
    with open(filename, 'r') as f:
        for line in f.readlines():
            l = line.strip()
            if not l:
                blank_lines.append(l)
            elif re.match(r'([\u4E00-\u9FA5]+$)|(^\d+)|(^#+)|(^\'\'\'$)',l):
                # 匹配中文/数字/#/''' 
                note_lines.append(l)
            else:
                code_lines.append(l)

def show_result():
    global code_lines
    global note_lines
    global blank_lines
    print('-'*20)
    print('code:', len(code_lines))
    for line in code_lines:
        print(line)
    print('-' * 20)
    print('note:', len(note_lines))
    for line in note_lines:
        print(line)
    print('-' * 20)
    print('blank:', len(blank_lines))
    code_lines.clear()
    note_lines.clear()
    blank_lines.clear()

def process_files(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.py'):
            print('='*30)
            print('current file:', os.path.join(path, file))
            findfile(os.path.join(path, file))
            show_result()

if __name__ == "__main__":
    process_files(os.getcwd())