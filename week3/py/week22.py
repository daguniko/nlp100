#! /usr/bin/python
# -*-coding:utf-8-*-
#(22) (21)のプログラムは破棄して，標準入力から英語のテキストを読み込み，ピリオド→スペース→大文字を文の区切りと見なし，１行１文の形式で標準出力に書き出せ．
#問題文の言っている意味がわからないので放置
import re
re_se = re.compile(r"(\n) [A-Z]")

f1 = open("../data/medline.txt").readlines()
f2 = open("../data/medline.txt.sent","w")


for line in f1:
    line = line.sprit()
    m = m.split(".")
    


#m = [m[0][0], m[0][1:]] + m[1:-1] + [m[-1][0:len(m[-1])-1], m[-1][-1]]

#for i in range(0, len(m)-1, 3):
#    print m[i]+m[i+1]+m[i+2]

# #単語に分割
# for line in f1:
#     line = line.split(".")
#     for i in range(len(line)):
#         line[i] = line[i].split()
#         for n in range(len(line[i])):
#             line[i][n] = line[i][n].split("[A-Z]")
#             f2.write(line[i][n][0] + "\n")
