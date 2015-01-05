#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(37) (36)の出力を読み込み，単語の連接の頻度を求めよ．ただし，出力形式は"(連接の頻度)\t(現在の単語)\t(次の単語)"とせよ．

from collections import Counter
f = open(u"../data/medline.txt.sent.tok.stem").readlines()


list = []
for line in f:
    line = line.split()
    list.append(line[1])

# 全連結の組み合わせ
print len(list) - 1

pre_word = ""
con = []
for word in list:
    if pre_word != "":
        con.append([pre_word,word])
    pre_word = word

fnl_con = []

word_count = {}
for word1,word2 in con:
    if word_count.has_key(word1) & word_count.has_key(word2):
        word_count[word1] += 1
        fnl_con.append([word1,word2,word_count[word1]])
    else:
        word_count[word1] = 1
        fnl_con.append([word1,word2,word_count[word1]])



print fnl_con

# print con
# print con[133][1]
# for i in range(1,133):
#     if con[133][1] == con[i][1]:
#         print con[i][1]

# print "in" in con[133][1]
