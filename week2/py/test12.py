#! /usr/bin/python
# -*-coding:utf-8-*-
#(12) 「なう」という文字列で終わるツイートを抽出せよ．

f = open(u'../data/tweet.txt').readlines()

# for line in f:
#     line = line.strip()
#     if line.endswith("なう") == True:
#         print line


#implementation by using regular expression 
import re

for line in f:
    line = line.strip()
    mex = re.search("なう$",line)
    if mex:
        print line
    
