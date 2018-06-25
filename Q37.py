dict1 = {"Name" : "John", "Age" : 23, "Batch" : "2014-C"}
dict2 = {"Name" : "Rex", "Age" : 21, "Batch" : "2013-B", "Section" : "B"}
dict3 = {"Name" : "Jeremy", "Age" : 28}

if len(dict1) > len(dict2) and len(dict1) > len(dict3):
    print "dict1 is biggest"
elif len(dict2) > len(dict3):
    print "dict2 is biggest"
else:
    print "dict3 is biggest"

dict1.update({"Major" : "Science"})
dict2.update({"Major" : "Arts"})
print "After adding new elements"
print "Dict1:", dict1
print "Dict2:", dict2

print "Dict1 length:", len(dict1)
print "Dict2 length:", len(dict2)
print "Dict3 length:", len(dict3)

dict1Str = str(dict1)
dict2Str = str(dict2)
dict3Str = str(dict3)
print "Conactenated string:", dict1Str + dict2Str + dict3Str
