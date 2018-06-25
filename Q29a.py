Str = "we love python"

print "Capitalize:", Str.capitalize()

print "Center:", Str.center(30, 'i')

print "Count:", Str.count('o', 4, 35)

encoded = Str.encode('base64', 'strict')
print "Encode:", encoded

print "Decode:", encoded.decode('base64', 'strict')
