#!/usr/bin/python

import math

class Circle:
	def area(self, radius):
		return math.pi*radius**2
	def circumference(self, radius):
		return 2*math.pi*radius

obj=Circle()

r=raw_input('Enter the radius of the circle')
print 'the area of the circle is',+obj.area(int(r))
print 'the circumference of the circle is',+obj.circumference(int(r))
