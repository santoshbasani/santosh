tup1 = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print "tup1:",tup1

tup2 = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print "tup2:",tup2

#concatenate tup1 with tup2
print "Concatenated tup1 and tup2:",tup1 + tup2

print "\n"

tup1 = (5, 6, 19, 10, 15)
tup2 = (55, 26, 191, 110, 215, 24, 16, 10)
tup3 = (125, 36, 19, 120, 155, 10, 55)

if len(tup1) > len(tup2) and len(tup1) > len(tup2):
    print "tup1 is greater"
elif len(tup2) > len(tup1):
    print "tup2 is greater"
else:
    print "tup3 is greater"

print "\n"

print "Before deleting each individual element we have:", tup1
tup1 = list(tup1)
for i in range(len(tup1)):
    tup1.pop()
tup1 = tuple(tup1)
print "After deleting each individual element we have:", tup1
del tup1
print tup1

print "\n"
print "Inserting new element in tuple after typecasting it to a list:"
tup1 = ()
tup1 = list(tup1)
for i in range(10):
    tup1.append(i)
tup1 = tuple(tup1)
print tup1
