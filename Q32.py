list1 = ["A", "B", "C", "D", "E"]
list2 = ["F", "G", "H", "I", "J", "K", "L", "M", "N"]
list3 = ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#length of each list
print "Length of list1:", len(list1)
print "Length of list2:", len(list2)
print "Length of list3:", len(list3)

#maximum and minimum of each list3
print "Max of list1:{0} Min of list1:{1}".format(max(list1), min(list1))
print "Max of list2:{0} Min of list2:{1}".format(max(list2), min(list2))
print "Max of list3:{0} Min of list3:{1}".format(max(list3), min(list3))

#compare each list
if len(list1) > len(list2) and len(list1) > len(list3):
    print "list1 is biggest"
elif len(list2) > len(list3):
    print "list2 is biggest"
else:
    print "list3 is biggest"

#deleting first and last element
list1 = list1[1:-1]
list2 = list2[1:-1]
list3 = list3[1:-1]

print "list1:", list1
print "list2:", list2
print "list3:", list3
