#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-

f = open(u"../data/medline.txt.sent.tok.stem").readlines()
line2 = ""

for line in f:
    line = line.split()
    if line2 != "":
        print line2 + "\t" + line[1]
    line2 = line[1]

