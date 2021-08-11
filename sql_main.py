#!/usr/bin/python python3

import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='learn_english')

cursor = connection.cursor()

sql = """INSERT INTO words(english,chinese,correct,incorrect)
         VALUES('separate','单独的',0,0)"""
try:
    cursor.execute(sql)
    connection.commit()
except:
    connection.rollback()
sql = """INSERT INTO words(english,chinese,correct,incorrect)
         VALUES('dotfile','配置文件',0,0)"""
try:
    cursor.execute(sql)
    connection.commit()
except:
    connection.rollback()
print(sql)
print("YES,Insert Successful.")
connection.close()
