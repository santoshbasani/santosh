import os

#finding all the files from current directory
for file in os.listdir("."):
    #finding sizr of each file
    size = os.stat(file).st_size
    #if file_size = 0 then print filename
    if(size == 0):
        print file
