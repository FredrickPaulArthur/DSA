def mergesort(alist):
    lefthalf, righthalf = [], []
    print('Splitting ',lefthalf, alist, righthalf)
    if len(alist)>1:
        mid=len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i,j,k=0,0,0
        
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i+=1
            else:
                alist[k]=righthalf[j]
                j+=1
            k+=1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i+=1
            k+=1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j+=1
            k+=1
    print("Merging ",lefthalf, alist, righthalf)

alist=[int(x) for x in input().split()]
mergesort(alist)
print(alist)