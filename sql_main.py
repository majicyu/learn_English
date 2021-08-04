#!/usr/bin/python python3

import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='learn_english')

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS words")

sql = """CREATE TABLE `words`(
    `id` int(10) NOT NULL AUTO_INCREMENT,
    `english` char(20) NOT NULL,
    `chinese` varchar(20) NOT NULL,
    `correct` int(10) DEFAULT NULL,
    `incorrect` int(10) DEFAULT NULL,
    PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;"""


cursor.execute(sql)
print("CREATE table successful.")
connection.close()
