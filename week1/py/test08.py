#! /usr/bin/python
# -*-coding:utf-8-*-
# (8) 各行を２コラム目の辞書順にソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）．

f = open(u'../data/address2.txt','r').readlines()
entire = []
entire2 = []
for line in f:
    itemline = line[:-1].split('\t')
    entire.append(itemline[-1])
    entire2.append(itemline[0])
    
entire3 = zip(entire2,entire)

entire3.sort(key = lambda t: t[1])

for a,b in entire3:
    print a + "\t" + b

