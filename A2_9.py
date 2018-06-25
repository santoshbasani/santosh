#!/usr/bin/python

import math

class Circle:
	def __init__(self,radius):
		self.r=radius
	def area(self):
		return math.pi*self.r**2
	def circumference(self):
		return 2*math.pi*self.r

obj=Circle(int(4))
print 'the area of the circle is',+obj.area()
print 'the circumference of the circle is',+obj.circumference()
