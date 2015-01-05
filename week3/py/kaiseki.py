#! /Users/sudo/.virtualenvs/hoge/bin/python2
# -*-coding:utf-8-*-

import pprint
import json
import corenlp

# パーサの生成
corenlp_dir = "/Users/sudo/.virtualenvs/hoge/bin/python2/Stanford"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

# パースして結果をpretty print
result_json = json.loads(parser.parse("I am Alice."))
pprint.pprint(result_json)
