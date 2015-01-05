#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(61) コーパスディレクトリ中の各ファイルに対して，cabochaを適用し，適当なディレクトリに係り受け解析の結果を格納せよ．ただし，各ファイルの文字コードがUTF-1n6LEであること，文区切りを自前で行う必要があることに注意せよ．

#regular expression part
import CaboCha
import os
import re
#set cabocha
c = CaboCha.Parser("-f1")


files = os.listdir("../data/corpus/");
prog = re.compile("\w.txt")
readlist = []

for file in files:
    result = prog.search(file)
    if result:
        readlist.append(file)

#MeCab part

for readfile in readlist:
    f = open(u"../data/corpus/" + readfile).readlines()
    f2 = open(u"../data/cabocha/" + readfile,"w")
    for line in f:
        m = c.parseToString(line)
        f2.write(m)
