#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
#-*-coding:utf-8-*-

from collections import defaultdict

class Morph:
    def __init__(self, surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self,num):
        self.num = num


one_chunk = Chunk("first")
print one_chunk
print one_chunk.num
