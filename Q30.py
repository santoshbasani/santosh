arr = []
N = int(input("Enter size of array:"))
temp = 0

for i in range(N):
    arr.append(int(input("Enter value:")))

for j in range(N):
    for k in range(N-1, j, -1):
        if (arr[k] < arr[k-1]):
            temp = arr[k]
            arr[k] = arr[k-1]
            arr[k-1] = temp

print "Sorted Array:", arr
