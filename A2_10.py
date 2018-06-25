#!/usr/bin/python

class First(object):
	def method1(self):
		print 'first'
class Second(First):
	def method1(self):
		print 'Second'
class Third(First):
	def method1(self):
		print 'Third'
class Fourth(Second, Third):
	def method1(self):
		print 'Fourth'

print 'First MRO',First.__mro__
print 'Second MRO',Second.__mro__
print 'Third MRO',Third.__mro__
print 'Fourth MRO',Fourth.__mro__

#First MRO (<class '__main__.First'>, <type 'object'>)
#Second MRO (<class '__main__.Second'>, <class '__main__.First'>, <type 'object'>)
#Third MRO (<class '__main__.Third'>, <class '__main__.First'>, <type 'object'>)
#Fourth MRO (<class '__main__.Fourth'>, <class '__main__.Second'>, <class '__main__.Third'>, <class '__main__.First'>, <type 'object'>)

