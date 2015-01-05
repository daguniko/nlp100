#! /usr/bin/python
# -*-coding:utf-8-*-
#(24) (23)のプログラムを修正し，各トークンの末尾が記号で終わる場合は，その記号を別のトークンとして分離せよ．
import re
p = re.compile("[!-/:-@[-`{-~]$")

f1 = open("../data/medline.txt.sent").readlines()
f2 = open("../data/medline.txt.sent.tok","w")

for line in f1:
    line = line.split()
    for i in line:
        match = p.search(i[-1])
        if match:
            f2.write(i[:-1]+"\n")
            f2.write(i[-1]+"\n")
        else :
            f2.write(i+"\n")

    f2.write("\n")
