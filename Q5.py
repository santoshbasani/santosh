def countFile():
    chars = lines = words = 0
    with open("input.txt" , "r") as inputfile:
        for line in inputfile:
            lines += 1
            words += len(line.split())
            chars += len(line)
    f = open("output.txt", "w")
    f.write("Lines: %s \nWords: %s \nCharacters: %s" %(lines,words,chars))

countFile()
