#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(41) 日本語の文章をMeCabで形態素解析し，その結果を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，１文は形態素（マッピング型）のリストとして表現せよ．
import MeCab
m = MeCab.Tagger("-Ochasen")
f = open(u"../data/japanese.txt").readlines()
dict = {}
sent = []
i = 0
for line in f:
    node = m.parseToNode(line)
    while node:
        print node.surface + "\n" + node.feature

        spl = node.feature.split(",")
        dict = {"surface":node.surface, "base":spl[6],"pos":spl[0],"pos1":spl[1]}
        sent.append(dict)
        node = node.next

    print line

#print one_sent[1][0]


# print one_sent[0]
# print one_sent[1]
# print one_sent[1]["base"]
# print one_sent[1]["pos"]
# print one_sent[1]["pos1"]
# print one_sent[1]["surface"]

#morphological analyis datas store the type of map








# string = u"それサバンナでも同じ事言えんの？"
# string = string.encode("utf-8")

# node = m.parseToNode(string)

# while node:
#     print node.surface, node.feature
#     node = node.next


