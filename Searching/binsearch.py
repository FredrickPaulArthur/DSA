def BinarySearch(sortedList, n, x):
    start = 0
    end = n-1
    while(start <= end):
        mid = (start + end) // 2
        if x == sortedList[mid]:
            return mid
        elif x < sortedList[mid]:
            end = mid-1
        elif x > sortedList[mid]:
            start = mid+1
    return -1

length = int(input("Enter the length of list :"))
sortedList = sorted(list(map(int, input().split())))
num_to_check = int(input("Number to check: "))
print(sortedList)

ans = BinarySearch(sortedList, length,num_to_check)
if ans == -1:
    print("Element not found")
else:
    print('Element found at index ${}'.format(ans))