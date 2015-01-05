#! /usr/bin/python
# -*-coding:utf-8-*-
#(17) 人名らしき表現にマッチする正規表現を各自で設計し，抽出せよ．（例えば「さん」「氏」「ちゃん」などの接尾辞に着目するとよい）

import re
f = open(u"../data/tweet.txt")
sea = re.compile(u"([ぁ-ん|一-龠|a-z|A-Z|ァ-ヴ]{2,5})(さん|くん|氏|ちゃん)")

for line in f:
    line = line.decode("utf-8")
    match = sea.search(line)
    if match:
        line = match.group()
        print line


