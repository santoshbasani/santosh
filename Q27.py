Str = raw_input("Enetr the string to be checked:")

revStr = ''.join(reversed(Str))

if (Str == revStr):
    print "Entered string is a pallindrome"
else:
    print "Entered string is NOT a pallindrome"
