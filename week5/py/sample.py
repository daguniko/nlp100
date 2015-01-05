#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(41) 日本語の文章をMeCabで形態素解析し，その結果を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，１文は形態素（マッピング型）のリストとして表現せよ．
import MeCab
m = MeCab.Tagger("-Ochasen")
string = u"それサバンナでも同じ事言えんの？"

# MeCabでUnicode文字列を扱う場合は、一度エンコードする必要がある。
# この際、
# node = tagger.parseToNode(string.encode("utf-8"))
# とすると、stringがパース中にガベコレされてしまって、
# 変な挙動になる場合があるので注意。このように一度変数に代入すれば問題ない。
string = string.encode("utf-8")
node = m.parseToNode(string)

# ノードを順番にたどる。
# node.surface, node.feature はstr型なので、
# この時点でunicode型に変換する方がトラブル防止のためにはいいかも。
while node:
    print node.surface, node.feature
    node = node.next


