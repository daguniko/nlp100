#! /usr/bin/python
# -*-coding:utf-8-*-
# (4) (3)で作ったcol1.txtとcol2.txtを結合し，元のタブ区切りテキストを復元したもの．確認にはpasteコマンドを用いよ．

f1 = open(u'../data/col1.txt','r').readlines()
f2 = open(u'../data/col2.txt','r').readlines()
f3 = open(u'../data/col3.txt','w')

for line,line2 in zip(f1,f2):
    itemlist = line.split('\n')
    itemlist2 = line2.split('\n')
    f3.write(itemlist[0] + "\t" + itemlist2[0] + "\n")
