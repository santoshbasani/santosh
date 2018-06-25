arr = [1,2,3,5,8]

print "Given array:", arr

item = input("Enter item to be found:")

first = 0
last = len(arr) - 1
flag = False

while (first <= last and not flag):
    mid = (first + last) / 2
    if arr[mid] == item:
        flag = True
        break
    else:
        if item < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1

if(flag):
    print "Success"
else:
    print "Unsuccessful search"
