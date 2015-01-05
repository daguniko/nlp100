#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(49) (48)の出力を利用して，文字列の頻度を横軸，その文字列の異なり数（種類数）を縦軸として，ヒストグラムをプロットせよ．なお，プロットにはgnuplotやmatplotlibを用い，グラフを画像ファイルとして保存せよ．


import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

f = open(u"../data/output.txt").readlines()

data = {}
for line in f:
    w,i = line.strip().split("\t")
    data[w] = int(i)

plt.rc('font', **{'family': 'serif'})
# キャンパス
fig = plt.figure()
# プロット領域(1x1分割の1番目に領域を配置する)
ax = fig.add_subplot(111)
# ヒストグラム(normedをTrueにすると確立表示になる)
ax.hist(data.values(), bins = len(data.values()),range=(0,150))
ax.set_title("histgram")
ax.set_ylabel("kotonari")
ax.set_xlabel("hindo")
ax.set_xlim(0,150)
ax.set_ylim(0,20)
plt.savefig("sample49.png")
plt.show()




