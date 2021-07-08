#!/usr/bin/python python3

from translate import Translator

fi = open("./words.txt","r")
fo = open("./words.sep.txt","w")

translator = Translator(to_lang="zh")

while True:
    s = fi.readline()
    if s == "":
        break
    num = en = enc = cn =""
    index = 0
    for char in s:
        if index== 0:
            if char == '、':
                index = 1
            else:
                num += char
        elif index == 1:
            en += char
            if char == ':':
                index = 2
        else:
            cn += char
    #print(num,en[:-1],cn)
    #translation = translator.translate(en)
    #print(translation[:-1])
    fo.writelines(num + '\n')
    fo.writelines(en[:-1] + '\n')
    fo.writelines(cn + '\n')
    #fo.writelines(<++> + '\n')
