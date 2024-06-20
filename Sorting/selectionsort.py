def selectionsort(l2):
    for i in range(len(l2)):
        least=i
        for k in range(i,len(l2)):
            if l2[k]<l2[least]:
                least=k
        swap(l2,least,i)

def swap(a,x,y):
    temp=a[x]
    a[x]=a[y]
    a[y]=temp

l1=[]
n=int(input('Size of list '))
for i in range(n):
    x=int(input())
    l1.insert(i,x)
print("Before sort ",l1)
selectionsort(l1)
print("After sort  ",l1)