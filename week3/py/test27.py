#! /usr/bin/python
# -*-coding:utf-8-*-
#(27) (10)のプログラムを呼び出すことで，頻度の高い英単語トップ100（単語と頻度がソートされたもの）を作成せよ．
#
#(10)のプログラムをモジュールとして読み込んで、ソートoリストをつくる練習
#
#(10) 各行の２コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べよ．ただし，(3)で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ．確認にはcut, uniq, sortコマンドを用いよ．

from collections import Counter
f = open(u'../data/medline.txt.sent.tok').readlines()

charlist1 = []
charlist2 = []

for line in f:
    itemlist = line[:-1].split('\t')
    charlist1.append(itemlist[0])
    charlist2.append(itemlist[-1])

charlist3 = zip(charlist1,charlist2)

charlist3.sort(key = lambda t:t[1])

data2 = charlist2

counter = Counter(charlist2)

for word, cnt in counter.most_common():
    print word, cnt 
