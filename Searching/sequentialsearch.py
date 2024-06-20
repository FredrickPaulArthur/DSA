def SequentialSearch(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos +=1
    return found, pos



n = int(input("Enter the size "))
l = []
for i in range(n):
    l.append(int(input()))
x = int(input("Enter the element to search "))

con, ind = SequentialSearch(l, x)

if con == True:
    print("Element found at index {}".format(ind))
else:
    print("Element not found")