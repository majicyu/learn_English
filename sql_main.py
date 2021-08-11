#!/usr/bin/python python3

import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='learn_english')

cursor = connection.cursor()

sql = "SELECT * FROM words where incorrect> %d" %(-1)
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        english = row[1]
        chinese = row[2]
        correct = row[3]
        incorrect = row[4]
        print("english=%s,chinese=%s,correct=%d,incorrect=%d" %(english,chinese,correct,incorrect))
except:
    import traceback
    traceback.print_exc()
    print("ERROR:unable to fetch data")
#print(sql)
print("YES,Select Successful.")
connection.close()
