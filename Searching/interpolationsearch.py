#If x is present in arr[0..n-1],then returns the index of it
#else returns -1
def interpolationsearch(arr,n,x):
    #Finds indices of two corners
    lo=0
    hi=(n-1)
    #Since array is sorted, an element present
    #in array must be in range defined by corner
    while lo<=hi and x>=arr[lo] and x<=arr[hi]:
        if lo==hi:
            if arr[lo]==x:
                return lo
            return -1
        #Probing the position with keeping
        #uniform distribution in mind
        pos=lo+int(((float(hi-lo)/(arr[hi]-arr[lo]))*(x-arr[lo])))
        #Condition of target found
        if arr[pos]==x:
            return pos
        #If x is larger,x is in upper part
        if arr[pos]<x:
            lo=pos+1
        #If x is smaller, x is in lower part
        else:
            hi=pos-1
    return -1

n=int(input("Enter the length of array "))
arr=[]
for i in range(n):
    arr.append(int(input()))
arr=sorted(arr)
print("Now the array is ",arr)
x=int(input("Enter the element to search "))

index=interpolationsearch(arr,n,x)

if index!=-1:
    print("Element found at index %d" %(index))
else:
    print("Element not found")