#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(63) 62の結果を用い，それぞれの名詞句のTF*IDF値を計算し，"(名詞句)\t(TF*IDF値)\t(TF値)\t(DF値)"の形式で出力せよ．ある名詞句wがあるとき，freq(w)をコーパス全体での名詞句wの出現頻度，df(w)を名詞句wが出現するファイルの数，Nを総ファイル数とし，TF*IDF値は freq(w) * log(N / df(w)) として計算せよ．

#regular expression part
import CaboCha
import os
import re
import nltk

#set cabocha
c = CaboCha.Parser("-f1")

files = os.listdir(u"../data/cabocha/");
prog = re.compile("\w.txt.n")
readlist = []

for file in files:
    result = prog.search(file)
    if result:
        readlist.append(file)

#MeCab part
inlist = []
outlist = [[]]

for readfile in readlist:
    f = open("../data/cabocha/" + readfile).readlines()
    previtem = ""
    for line in f:
        line = line.strip()
        inlist.append(line.decode("utf-8"))
    outlist.append(inlist)
    inlist = []

del outlist[0]

collection = nltk.TextCollection(outlist)
uniqTerms = list(set(collection))

#print
for doc in outlist:
    print "===================="
    for term in uniqTerms:
        print "%s\t%f\t%s\t%s" % (term, collection.tf_idf(term, doc),collection.tf(term,doc),collection.idf(term,doc))
    print "===================="

#write file
f2 = open("../data/cabocha/log.txt","w")

for doc in outlist:
    f2.write("====================\n".decode("utf-8"))
    for term in uniqTerms:
        #wsen = "%s\t%f\t%f\t%f" % (term,collection.tf_idf(term,doc),collection.tf(term,doc),collection.idf(term,doc))
        print term
        term = term.decode("utf-8")
        f2.write(term)
        f2.write("\t")
        f2.write(collection.tf_idf(term,doc))
        f2.write("\t")
        f2.write(collection.tf(term,doc))
        f2.write("\t")
        f2.write(collection.idf(term,doc))
        f2.write("\n")
        f2.write("====================\n")

