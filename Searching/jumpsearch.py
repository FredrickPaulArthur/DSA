import math
def jumpsearch(arr,x,n):
    #Finding block size to be jumped
    step=math.sqrt(n)
    #Finding the block where element is present
    #(if it is present)
    prev=0
    while arr[int(min(step,n)-1)]<x:
        prev=step
        step+=math.sqrt(n)
        if prev>=n:
            return -1
    #Doing a linear search for x in block
    #beginning wuth new
    while arr[int(prev)]<x:
        prev+=1
        #If we reached next block or end of array,
        #element is not present
        if prev==min(step,n):
            return -1
    #If element is found
    if arr[int(prev)]==x:
        return prev
    return -1

n=int(input("Enter the length of array "))
arr=[]
for i in range(n):
    arr.append(int(input()))
x=int(input("Enter the element to search "))
arr=sorted(arr)
print("Now the array is ",arr)
#Find the index of x using jumpsearch
index=jumpsearch(arr,x,n)

if index!=-1:
    print("Element found at index %d" %(index))
else:
    print("Element not found")