#! /usr/bin/python
# -*-coding:utf-8-*-
#(11) 「拡散希望」という文字列を含むツイートを抽出せよ．

f = open(u'../data/tweet.txt').readlines()

for line in f:
    line = line.strip()
    if line.find("拡散希望") >= 0:
        print line

