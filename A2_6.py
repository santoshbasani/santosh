#!/usr/bin/python
class Add:
	def add(self,datatype,Q,W):
		if datatype =='int':
			R=0
			R=Q+W
			print R
		if datatype =='matrix':
			R = [[0,0],[0,0]]
			for i in range(len(X)):
   				for j in range(len(X[0])):
       					R[i][j] = X[i][j] + Y[i][j]
			for r in R:
   				print(r)
obj=Add()			
a=5
b=6
X = [[12,7],
     [4 ,5]]

Y = [[5,8],
     [6,7]]

obj.add('matrix',X,Y)
obj.add('int',a,b)

