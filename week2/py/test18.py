#! /usr/bin/python
# -*-coding:utf-8-*-
#(18) 仙台市の住所らしき表現にマッチする正規表現を各自で設計し，抽出せよ．

import re

f = open(u"../data/tweet.txt").readlines()
sr = re.compile(u"([一-龠]){2,5}市")

for line in f:
    line = line.decode("utf-8")
    match = sr.search(line)
    if match:
        line = match.group()
        print line
