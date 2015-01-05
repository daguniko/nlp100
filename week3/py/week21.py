#! /usr/bin/python
# -*-coding:utf-8-*-
#(21) 標準入力から英語のテキストを読み込み，ピリオドを文の区切りと見なし，１行１文の形式で標準出力に書き出せ．

f1 = open("../data/medline.txt").readlines()
f2 = open("../data/medline.txt.sent","w")

for line in f1:
    #line[:-1]をすることで、lineのリストの最後の文字列"\n"を削除することが出来る
    line = line[:-1].split(".")
    for i in line:
        f2.write(i + ".\n")

