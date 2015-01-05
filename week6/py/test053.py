#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(53) 文節を表すクラスChunkを実装せよ．このクラスは形態素のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，(51)の解析結果を１文毎に読み込み，１文をChunkオブジェクトのリストとして表現し，適当に表示するプログラムを実装せよ．

from collections import defaultdict
import CaboCha
import re
c = CaboCha.Parser("-f1")
f = open(u"../data/cabocha_japanese.txt")

class Chunk:
    def __init__(self,num,morphs,dst,scrs):
        self.num = num
        self.morphs = morphs
        self.dst = dst
        self.scrs = scrs

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def test052():
    all_list = []
    one_list = []
    one_sent = []
    all_sent = []
    kakari_dict = defaultdict(list)
    for line in f:
        if "\t" in line:
            item = re.split(r"\t|,",line.strip())
            one_chunk.morphs.append(Morph(item[0],item[7],item[1],item[2]))
        elif "EOS" in line:
            for one_chunk in one_sent:
                one_chunk.scrs = kakari_dict[one_chunk.num]
                for morphs in one_chunk.morphs:
                    print "surface=%s\tbase=%s\tpos=%s\tpos1=%s" % (morphs.surface,morphs.base,morphs.pos,morphs.pos1)
                print "num=%s\tdst=%s\tscrs=%s" % (one_chunk.num,one_chunk.dst,one_chunk.scrs)

            all_list.append(one_list)
            all_sent.append(one_sent)
            print "EOS"
            print ""
            one_list = []
            one_sent = []
            kakari_dict = defaultdict(list)

        elif "*" in line:
            item2 = line.split()
            item2[2] = item2[2][:-1]
            one_chunk = Chunk(item2[1],[],item2[2],[])
            kakari_dict[item2[2]].append(item2[1])
            one_sent.append(one_chunk)



if __name__  == '__main__':
    test052()

