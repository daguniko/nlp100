#! /usr/bin/python
# -*-coding:utf-8-*-
#(28) 各単語から文字バイグラムを抽出するプログラムを実装せよ．また，(27)と同様の方法で，頻度の高い文字バイグラムトップ100（バイグラムと頻度がソートされたもの）を作成せよ．
#(10) 各行の２コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べよ．ただし，(3)で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ．確認にはcut, uniq, sortコマンドを用いよ．

import re
re_se = re.compile(r"")

from collections import Counter
f = open(u'../data/medline.txt.sent.tok').readlines()
re_se = re.compile(r"(\w)(\1)+")

charlist1 = []

for line in f:
    match = re_se.search(line)
    if match:

        # +1 をすることで、タブの部分も削除して出力する
        sta = line.find("\t") + 1
        strin = line[sta:].strip()
        charlist1.append(strin)

counter = Counter(charlist1)
for word,cnt in counter.most_common():
    print word+"\t" +str(cnt)
