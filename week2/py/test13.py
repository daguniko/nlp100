#! /usr/bin/python
# -*-coding:utf-8-*-
#(13) 非公式RTのツイートの中で，RT先へのコメント部分のみを抽出せよ．

f = open(u'../data/tweet.txt').readlines()

for line in f:
    line = line.strip()    
    if line.find("RT @") >= 0:
        startsearch = line.find(":") + 1
        endsearch = line.find("RT @") 
        if len(line[startsearch:endsearch]) > 2:
            print line[startsearch:endsearch]
