from string import maketrans

Str = "we love python"

tran = maketrans("aeiou", "12345")
print "translate()", Str.translate(tran)

print "upper()", Str.upper()

print "zfill()", Str.zfill(40)

print "title()", Str.title()

print "isdecimal()", Str.isdecimal()
