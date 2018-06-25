#!/usr/bin/python
class Compare:
	def __init__(self, strval):
		self.X=strval
	def __gt__(self,other):
		if len(self.X)>len(other):
			print 'the provided string is shorter in length'
		elif len(self.X)==len(other):
			print 'the strings are equal in lenth'
		else:
			print 'the provided string is longer in length'

obj=Compare("Deependra")
obj.__gt__("Thagunna")
