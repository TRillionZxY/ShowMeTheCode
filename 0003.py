'''
0003/0025
将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中
'''
import redis
import re

def make_connect():
    r = redis.Redis(host='', port=)
    return r

def upload_database():
    session = make_connect()
    with open('coupon.txt', 'r') as file:
        for line in file.readlines():
            c_id = re.findall(r'^\d{3}', line)
            c_id = list(map(int, c_id))
            session.set(c_id[0], line.strip())

if __name__ == "__main__":
    upload_database()