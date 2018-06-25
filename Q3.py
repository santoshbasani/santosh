count_e = 0
input_string = raw_input("Enter string:")

for c in input_string:
    if "e" in c:
        count_e += 1

if count_e == 2:
    print 'True'
else:
    print 'False'
