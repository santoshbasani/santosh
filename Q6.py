#three lists
list1 = [45, 60, 32, 99, 125]
list2 = [65, 78, 90, 43, 22]
list3 = [20, 10, 50, 20, 60]

#max and min list declaration
maxlist = []
minlist = []

avgMin = avgMax = 0

#function to find first and second largest
def FirstSecondLarge(list):
    first = second = None
    for n in list:
        if n > first:
            first, second = n, first
        elif first > n > second:
            second = n
    maxlist.extend([ first, second])

FirstSecondLarge(list1)
FirstSecondLarge(list2)
FirstSecondLarge(list3)

#function to find first and second smallest
def FirstSecondSmall(list):
    first = second = float('inf')
    for n in list:
        if n <= first:
            first, second = n, first
        elif n < second:
            second = n
    minlist.extend([first, second])

FirstSecondSmall(list1)
FirstSecondSmall(list2)
FirstSecondSmall(list3)

#average of both lists
print "Max List Average = " , sum(maxlist) / len(maxlist)
print "Min List Average = " , sum(minlist) / len(minlist)
