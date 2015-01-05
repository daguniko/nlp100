#! /usr/bin/python
# -*-coding:utf-8-*-
# (3) 各行の１列目だけを抜き出したものをcol1.txtに，２列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

f = open(u'../data/address.txt','r').readlines()
f1 = open(u'../data/col1.txt','w')
f2 = open(u'../data/col2.txt','w')
for line in f:
    itemlist = line.split('\t')
    f1.write(itemlist[0]+"\n")
    f2.write(itemlist[-1]+"\n")
