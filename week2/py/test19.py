#! /usr/bin/python
# -*-coding:utf-8-*-
#(19) 郵便番号・県名・市町村名の３要素を組で（まとめて）抽出せよ．

import re
f = open(u"../data/tweet.txt").readlines()

sr = re.compile(u"([一-龠]{2,3})県")
sr2 = re.compile(u"([一-龠]{2,5})市")
sr3 = re.compile(u"[1-9]{3}-[1-9]{4}")

for line in f:
    line = line.decode("utf-8")
    match = sr.search(line)
    if match:
        print match.group()
    match = sr2.search(line)
    if match:
        print match.group()
    match = sr3.search(line)
    if match:
        print match.group()

