def insertionsort(l1):
    for i in range(1,len(l1)):
        currentvalue=l1[i]
        position=i
        while position>0 and l1[position-1]>currentvalue:
            l1[position]=l1[position-1]
            position=position-1
        l1[position]=currentvalue

l=[]
n=int(input("Enter the size of the list "))
for i in range(n):
    x=int(input())
    l.insert(i,x)
print("Before sort ",l)
insertionsort(l)
print("After sort  ",l)