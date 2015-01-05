#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(35) 辞書引きを行った結果，３つ以上のエントリが見つかったもののみを出力せよ．

import marshal

f1 = open(u"../data/medline.txt.sent.tok.stem")
f2 = open(u"../data/mapfile","r")

map = marshal.load(f2)

print "Key一覧"
print map.keys()


for line in f1:
    line = line.split()
    if line[0] in f2:
        print ""
    else:
        print line[0] + "\tx"

