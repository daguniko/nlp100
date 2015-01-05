#! /usr/bin/python
# -*-coding:utf-8-*-
#(16) 括弧表現のうち，括弧の内側がアルファベット大文字の文字列，括弧の左側が漢字の文字列のものを抽出せよ．このとき，括弧の左側の表現と括弧の内側の表現をタブ区切り形式で出力せよ．

import re
f = open(u"../data/tweet.txt").readlines()

for line in f:
    match = re.search("[一-龠]+\([A-Z]+\)",line)
    if match:
        line = match.group()
        print line
