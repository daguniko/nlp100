#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(52) 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，(51)の解析結果を１文毎に読み込み，１文をMorphオブジェクトのリストとして表現し，適当に表示するプログラムを実装せよ．

import CaboCha
import re
c = CaboCha.Parser("-f1")
f = open(u"../data/cabocha_japanese.txt")
class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def test052():
    all_list = []
    one_list = []
    for line in f:
        if line[0] != "*":
            if "\t" in line:
                item = re.split(r"\t|,",line.strip())
                one_list.append(Morph(item[0],item[7],item[1],item[2]))
            elif "EOS" in line:
                for item in one_list:
                    print "surface=%s\tbase=%s\tpos=%s\tpos1=%s" % (item.surface,item.base,item.pos,item.pos1)
                all_list.append(one_list)
                print "EOS"
                one_list=[]


if __name__  == '__main__':
    test052()

