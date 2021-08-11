#!/usr/bin/python python3

import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='learn_english')

cursor = connection.cursor()

sql = "UPDATE words set correct = correct+1 where incorrect = %d" %(0)
try:
    cursor.execute(sql)
    connection.commit()
except:
    connection.rollback()
#print(sql)
print("YES,UPDATE Successful.")
connection.close()
