#!/usr/bin/python
import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
d=int(sys.argv[4])
e=int(sys.argv[5])

print "First parameter in command line",a
print "Second parameter in command line",b
print "Third parameter in command line",c
print "Fourth paramenter in command line",d
print "Fifth parameter in command line",e

if a>b and a>c:
    print "Value A:%d is larger"%a
elif b>a and b>c:
    print "Value B:%d is Larger"%b
else:
    print "Value C:%d is Larger"%c
