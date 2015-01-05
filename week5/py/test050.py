#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(50) (48)の出力を利用して，文字列の出現頻度の順位（高い順）を横軸，その出現頻度を縦軸として，プロットせよ．


import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

f = open(u"../data/output.txt").readlines()

data = {}
listx,listy=[],[]
j = 0

for line in f:
    w,i = line.strip().split("\t")
    data[w] = int(i)
    if j < 100:
        listx.append(j)
        listy.append(int(i))
    j+=1

plt.rc('font', **{'family': 'serif'})
# キャンパス
fig = plt.figure()
# プロット領域(1x1分割の1番目に領域を配置する)
ax = fig.add_subplot(111)
# ヒストグラム(normedをTrueにすると確立表示になる)
plt.plot(listx,listy)
ax.set_title("histgram")
ax.set_ylabel("hindo")
ax.set_xlabel("kotonari")
ax.set_xlim(0,100)
ax.set_ylim(0,300)
plt.savefig("sample50.png")
plt.show()

