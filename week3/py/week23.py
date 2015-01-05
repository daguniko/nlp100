#! /usr/bin/python
# -*-coding:utf-8-*-
#(23) (22)の出力を標準入力から１行（１文）を読み込む毎に，スペースで単語列に分割し，１行１単語形式で標準出力に書き出せ．文の終端を表すため，文が終わる毎に空行を出力せよ．

f1 = open("../data/medline.txt.sent").readlines()
f2 = open("../data/medline.txt.sent.tok","w")

for line in f1:
    line = line.split()
    for i in line:
        f2.write(i+"\n")
    f2.write("\n")




