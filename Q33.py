myList = [10,20,30,40,50,60,70]

#append 80
myList.append(80)
print "Append 80:",myList

#insert 100 at 4th pos
myList.insert(4, 100)
print "Insert 100 at 4th pos:",myList

#sorting list
myList.sort()
print "Sorted list:", myList

#sorting list in descending order
myList.sort(reverse=True)
print "Descending order:", myList

#pop last 3 elements
for i in range(3):
    myList.pop()
print "Popped last 3 ele:", myList
