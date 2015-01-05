#! /usr/bin/python
# -*-coding:utf-8-*-
# (5) 自然数Nをコマンドライン引数にとり，入力のうち先頭のN行だけ．確認にはheadコマンドを用いよ．

import sys
import numbers
f = open(u'../data/address.txt','r').readlines()

#error handling
if len(sys.argv) == 1:
    sys.argv.append(10)
elif len(sys.argv) > 2:
    print "第一引数のみを入力をしてください。"
    sys.exit()

for line in f[0:int(sys.argv[1])]:
    line = line.split("\n")
    print line[0]
