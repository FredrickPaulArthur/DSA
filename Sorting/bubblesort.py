def printList(a):
    for i in range(n-1):
        print(a[i], end=' ')
    print(a[i+1])
def bubbleSort(a):  
    for i in range(0,len(a)-1):  
        for j in range(len(a)-1):  
            if(a[j]>a[j+1]):  
                temp = a[j]  
                a[j] = a[j+1]  
                a[j+1] = temp
        printList(a)

n = int(input())
a = list(map(int,input().split()))  
bubbleSort(a)