'''
0001/0025
为你的应用生成激活码（或者优惠券）
使用 Python 如何生成 200 个激活码（或者优惠券）
'''
import random
import string

key = string.ascii_letters + string.digits 
# 'a-z and A-Z' '0123456789'

def get_coupon(count):
    coupon = ''
    for _ in range(count):
        coupon += random.choice(key)
    return coupon

def save_coupon(data):
    with open('coupon.txt', 'a+') as file:
        file.write(data+'\n')

def get_key(count1, count2):
    #count1: number of key
    #count2: length of key
    for i in range(count1):
        data = '%03d' % i
        #add No. to key insure it’s uniqueness
        data += get_coupon(count2)
        save_coupon(data)
        print(data)
        
if __name__ == '__main__':
    get_key(200,10)
    
    