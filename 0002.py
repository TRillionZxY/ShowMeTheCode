'''
0002/0025
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
'''
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import re

Base = declarative_base()

DB_info = {
    'user': 'root',
    'password': ' ',
    'ip': '127.0.0.1',
    'port': '3306',
    'database': 't1'
}

class Coupon(Base):
    __tablename__ = 'coupon'

    id = Column(String(5), primary_key=True)
    code = Column(String(10))

def make_connect(DB_info):
    connect_str = 'mysql+mysqlconnector://{user}:{password}@{ip}:{port}/{database}'.format_map(DB_info)
    engine = create_engine(connect_str)
    DBSession = sessionmaker(engine)
    session = DBSession()
    return session

def upload_database():
    session = make_connect(DB_info)
    with open('coupon.txt', 'r') as file:
        for line in file.readlines():
            c_id = re.findall(r'^\d{3}', line)
            c_id = list(map(int, c_id))
            # print(c_id)    
            session.add(Coupon(id=c_id[0], code=line))
        session.commit()
        session.close()

if __name__ == "__main__":
    upload_database()
