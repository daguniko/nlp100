#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(48) 標準入力から読み込んだ各行の文字列の頻度を求めるプログラムを書き，(47)のプログラムと組み合わせることによって，文章中に出現する各動詞の出現頻度を求めよ．さらに，出現頻度の高い順に動詞を並べよ．
from collections import Counter

import argparse

parser = argparse.ArgumentParser()


#必須オプション
parser.add_argument("-f", "--file", help="read file", required=True)

#スイッチ
parser.add_argument("-v", "--verbs", help="extract all verbs", action = "store_true")
parser.add_argument("-b", "--basic", help="extract all basic of verbs", action = "store_true")
parser.add_argument("-s", "--sahen", help="extract all sahen nouns", action = "store_true")
parser.add_argument("-r", "--renketu", help="extract expression like 'A no B'", action = "store_true")
parser.add_argument("-m", "--mren", help="extract all linked nouns", action = "store_true")

#任意オプション
#parser.add_argument("-b", "--basic", help="extract all basic of verbs")

#version表示オプション
parser.add_argument("--version", action = "version", version="%(prog)s 2.0")

args= parser.parse_args()

#output selection
#print "出力先を入力してください"
#output = raw_input()

#f2 = open(output,"w")

#MeCab
import MeCab
m = MeCab.Tagger("-Ochasen")
f = open(args.file).readlines()

dict = {}

i = 0
sverblist = [["",""]]
pre_list = ["",""]
verblist = [["",""]]
basiclist = []
sahenlist = []
renlist = []

for line in f:
    node = m.parseToNode(line)
    while node:

        spl = node.feature.split(",")
        dict = {"surface":node.surface, "base":spl[6],"pos":spl[0],"pos1":spl[1]}
        print node.surface,node.feature
        if spl[0] == "動詞":
                verblist.append([node.surface,spl[5]])
                basiclist.append(spl[6])

        if spl[0] == "名詞" and spl[1] == "サ変接続":
            sahenlist.append(node.surface)

        if spl[0] == "名詞":
            node2 = node.next
            spl2 = node2.feature.split(",")
            dict = {"surface":node2.surface, "base":spl2[6],"pos":spl2[0],"pos1":spl2[1]}

            if spl2[0] == "名詞":
                sverblist.append([node.surface,node2.surface])

            if node2.surface == "の":
                node3 = node2.next
                spl3 = node3.feature.split(",")
                dict = {"surface":node3.surface, "base":spl3[6],"pos":spl3[0],"pos1":spl3[1]}

                if spl3[0] == "名詞":
                    renlist.append(node.surface + node2.surface + node3.surface)




        node = node.next

    i = i + 1
    print line


print "basiclist"
counter = Counter(basiclist)

for word,cnt in sorted(counter.most_common(), key=lambda x:x[1], reverse = True):
    print word,cnt

print "\nverblist"
verblist2 = []
for i in range(len(verblist)):
    verblist2.append(verblist[i][0])

counter2 = Counter(verblist2)




kazulist = []
prepare = []

for i in range(len(verblist)):
    if verblist[i][0] == "いる":
        prepare.append(verblist[i][1])

prepare = list(set(prepare))
print prepare[0]
print len(prepare)



for word,cnt in sorted(counter2.most_common(), key=lambda x:x[1], reverse = True):
    print word,cnt


    #f2.write(word+"\t"+str(cnt)+"\n")






if args.verbs:
    print "verb list"
    for i in range(len(verblist)):
        print verblist[i]

if args.basic:
    print "basic list"
    for i in range(len(basiclist)):
        print basiclist[i]

if args.sahen:
    print "sahen list"
    for i in range(len(sahenlist)):
        print sahenlist[i]

if args.renketu:
    print "'名詞'の'名詞' list"
    for i in range(len(renlist)):
        print renlist[i]

if args.mren:
    print "all linked renketu list"
    for i in range(len(sverblist)):
        if pre_list[1] == sverblist[i][0]:
            print sverblist[i][1],
        else:
            print ""
            print sverblist[i][0],
            print sverblist[i][1],


        pre_list[0] = sverblist[i][0]
        pre_list[1] = sverblist[i][1]





