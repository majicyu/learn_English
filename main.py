#!/usr/bin/python python3

import os
import pinyin
import random
import pdb
class Sentence:
    def __init__(self,num,en,cn):
        self.num = num.strip()
        self.en = en.strip()
        self.cn = cn.strip()

sentences = []

fi = open("./words.sep.txt","r")
sum = 0

while True:
    num = fi.readline()
    if num == "":
        break
    en = fi.readline()
    cn = fi.readline()
    _ = fi.readline()
    #print(num,en,cn, sep='',end='\n')
    new_sentence = Sentence(num,en,cn)
    sentences.append(new_sentence)
    sum += 1

print(sentences[0].num)

pdb.set_trace()
os.system("clear")
for sentence in sentences:
    random_number = random.randint(1,sum)
    while True:
        print(sentence.en)
        ans = input("Chinese:")
        if ans == sentence.cn or ans == pinyin.get(sentence.cn,format="strip",delimiter=""):
            print("Correct!")
            _ = input(" --- Press enter to continue --- ")
            os.system("clear")
            break
        else:
            print("Incorrect!")
            reveal = input(" ---Press enter to continue, y to reveal the answer ---")
            if reveal == "y":
                print(sentence.cn)
                _ = input(" ---Press enter to continue--- ")
            os.system("clear")
