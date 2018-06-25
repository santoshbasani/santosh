tup1 = ("Table", "Chair", "Window")
tup2 = ("Mobile", "Telephone", "WiFi", "Router", "Dashboard")

#Built-in function for tuple
#1 cmp()
print cmp(tup1, tup2)

#2 len()
print "Length of tup1:", len(tup1)
print "Length of tup2:", len(tup2)

#3 max()
print "Max of tup1", max(tup1)
print "Max of tup2", max(tup2)

#4 min()
print "Min of tup1", min(tup1)
print "Min of tup2", min(tup2)

#5tuple()
myList = ["Bottle", "Pencil", "Sharpner", "Eraser"]
myTuple = tuple(myList)
print "Using tuple() function", myTuple
