
#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(60) (57)の出力を「係り元」→「係り先」の有向グラフとみなし，Graphvizを使ってグラフを描画せよ．すなわち，(57)の出力をGraphvizの入力フォーマットであるDOT形式に変換するプログラムを実装すればよい．グラフを描画するときは「neato -Tsvg」コマンドを用い，SVG形式に書き出すとよい．
import pygraphviz as pgv
f1 = open("../data/test57.txt","w")

from test054 import *
def test56_morph(all_sent_list):
    print all_sent_list
    for one_sent_list in all_sent_list:
        for one_chunk in one_sent_list:
            for another_chunk in one_sent_list:
                if one_chunk.num == another_chunk.dst:
                    s = one_chunk.morphs_pos("動詞")
                    s3 = one_chunk.morphs_pos1("非自立")
                    s2 = another_chunk.morphs_pos("名詞")
                    s4 = another_chunk.morphs_pos1("非自立")
                    if s and s2:
                        if s3 or s4:
                            pass
                        else:
                            print another_chunk.morphs_add + "\t" +one_chunk.morphs_add
                            f1.write(another_chunk.morphs_add)
                            f1.write("\t")
                            f1.write(one_chunk.morphs_add)
                            f1.write("\n")

if __name__ == '__main__':
	all_sent_list=test54_morph("../data/cabocha_japanese.txt")
	test56_morph(all_sent_list)
