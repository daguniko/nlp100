#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(51) 日本語の文章をCaboChaで係り受け解析し，ラティス形式（-f1オプション）の解析結果を得よ．
import CaboCha
c = CaboCha.Parser("-f1")
f = open(u"../data/japanese.txt").readlines()
for line in f:
    m = c.parseToString(line)
    print m
