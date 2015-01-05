#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(62) 61で作成した各ファイルから，名詞句（文節中の名詞の連接）を抜き出して，個別のファイルに格納せよ．

#regular expression part
import CaboCha
import os
import re
#set cabocha
c = CaboCha.Parser("-f1")

files = os.listdir("../data/cabocha/");
prog = re.compile("\w.txt")
readlist = []

for file in files:
    result = prog.search(file)
    if result:
        readlist.append(file)

#MeCab part

for readfile in readlist:
    f = open(u"../data/cabocha/" + readfile).readlines()
    f2 = open(u"../data/cabocha/" + readfile + ".n","w")
    previtem = ""
    for line in f:
        if "\t" in line:
            item = re.split(r"\t|,",line.strip())
            if previtem == "名詞" and item[1] == "名詞":
                print prevline + item[0]
                f2.write(prevline+item[0] + "\n")
            prevline = item[0]
            previtem = item[1]
