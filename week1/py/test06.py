#! /usr/bin/python
# -*-coding:utf-8-*-
# (6) 自然数Nをコマンドライン引数にとり，入力のうち末尾のN行だけ．確認にはtailコマンドを用いよ．

import sys
f = open(u'../data/address.txt','r').readlines()

#error handling
if len(sys.argv) == 1:
    sys.argv.append(10)
elif len(sys.argv) > 2:
    print "第一引数のみを入力をしてください。"
    sys.exit()

for line in f[len(f) - int(sys.argv[1]):]:
    line = line.split('\n')
    print line[0]
