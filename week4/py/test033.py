#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(33) (32)で作成した辞書を読み込み，１行１単語形式（例えばmedline.txt.sent.tok.stem）で標準入力から読み込んだ単語に対して，辞書引き結果を付与するプログラムを実装せよ．

import marshal

f1 = open(u"../data/medline.txt.sent.tok.stem")
f2 = open(u"../data/mapfile","r")

map = marshal.load(f2)

print "Key一覧"
print map.keys()


for line in f1:
    line = line.split()
    if line[0] in f2:
        print line[0] + "\to" 
    else :
        print line[0] + "\tx"






