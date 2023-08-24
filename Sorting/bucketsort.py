def insertionsort(b):
    for i in range(1,len(b)):
        up=b[i]
        j=i-1
        while j>=0 and b[j]>up:
            b[j+1]=b[j]
            j-=1
        b[j+1]=up
    return b

def bucketsort(x):
    arr=[]
    slot_num=int(input("Enter the number of slots "))
    for i in range(slot_num):
        arr.append([])
    #Put array elements in different buckets
    for j in x:
        index_b=int(slot_num*j)
        arr[index_b].append(j)
    #Sort individual buckets
    for i in range(slot_num):
        arr[i]=insertionsort(arr[i])
    #Concatenate the result
    k=0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k]=arr[i][j]
            k+=1
    return x

n=int(input("Enter the size of array "))
x=[]
for i in range(n):
    x.append(float(input()))
print("Sorted Array is ",bucketsort(x))