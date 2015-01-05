#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-
#(60) (57)の出力を「係り元」→「係り先」の有向グラフとみなし，Graphvizを使ってグラフを描画せよ．すなわち，(57)の出力をGraphvizの入力フォーマットであるDOT形式に変換するプログラムを実装すればよい．グラフを描画するときは「neato -Tsvg」コマンドを用い，SVG形式に書き出すとよい

"""出力形式
digraph knock60{
\t"" -> "";
}"""


f1 = open("../data/test.dot","w")

def test60():
        f1.write("digraph knock60{\n")
	#print "digraph knock60{"
	for line in open("../data/test57.txt"):
		#item = line.replace('\"',r'\"')
		item = line.split("\t")
		#print '\t"%s" -> "%s";' % (item[0],item[1])
                #f1.write('\t"%s" -> "%s";\n') % (item[0],item[1])
                f1.write ('\t"%s" -> "%s";' % (item[0],item[1]))
        f1.write("}")
	#print "}"


if __name__ == '__main__':
	test60()
