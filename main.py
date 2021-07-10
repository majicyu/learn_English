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
sum = -1

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

#pdb.set_trace()
os.system("clear")
#for sentence in sentences:
#random_number = random.randint(1,sum)
isError = "false"
while True:
    #print(sentence.en)
    if isError == "false":
        random_number = random.randint(0,sum)
    print(sentences[random_number].en)
    ans = input("Chinese:")
    #if ans == sentence.cn or ans == pinyin.get(sentence.cn,format="strip",delimiter=""):
    if ans == sentences[random_number].cn or ans == pinyin.get(sentences[random_number].cn,format="strip",delimiter=""):
        print("Correct!")
        isError = "false"
        #_ = input(" --- Press enter to continue --- ")
        #os.system("clear")
        #break
    else:
        print("Incorrect!")
        isError = "true"
        reveal = input(" ---Press enter to continue, y to reveal the answer ---")
        if reveal == "y":
            #print(sentence.cn)
            print(sentences[random_number].cn)
            #_ = input(" ---Press enter to continue--- ")
        #os.system("clear")
    isContinue = input(" --- Press enter to continue, n to end ---")
    if isContinue == "n":
        os.system("clear")
        break
    else:
        os.system("clear")
        continue
