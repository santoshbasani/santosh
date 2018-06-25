maxList = []
minList = []

def findMaximum(myList):
    temp1, temp2 = None, None
    for i in myList:
        if i > temp1:
            temp1, temp2 = i, temp1
        elif temp1 > i > temp2:
            temp2 = i
    maxList.extend([temp1, temp2])

def findMinimum(myList):
    temp1, temp2 = float('inf'), float('inf')
    for i in myList:
        if i <= temp1:
            temp1, temp2 = i, temp1
        elif i < temp2:
            temp2 = i
    minList.extend([temp1, temp2])

list1 = [2, 5, 6 ,1, 10]
list2 = [22, 35, 16 ,11, 9, 10, 14, 29, 45]
list3 = [12, 15, 16 ,12, 210, 330, 63]

#creating maxlist
findMaximum(list1)
findMaximum(list2)
findMaximum(list3)
print maxList

#average of maxList
print "Average of Maxlist:", sum(maxList) / len(maxList)

#creating minList
findMinimum(list1)
findMinimum(list2)
findMinimum(list3)
print minList
#average of minList
print "Average of Minlist:", sum(minList) / len(minList)
