a = 0
e = 0
i = 0
o = 0
u = 0
numofvowels = 0

Str = raw_input("Enter the string:")

for eachC in Str:
    if eachC == 'a':
        numofvowels += 1
        a += 1
    elif eachC == 'e':
        numofvowels += 1
        e += 1
    elif eachC == 'i':
        numofvowels += 1
        i += 1
    elif eachC == 'o':
        numofvowels += 1
        o += 1
    elif eachC == 'u':
        numofvowels += 1
        u += 1

print "Number of vowels:", numofvowels
print "a:", a
print "e:", e
print "i:", i
print "o:", o
print "u:", u
