n=int(input("Enter the total number of entries: "))
number=list(map(int,input().split()))
num_to_check=int(input("Enter the number to check: "))
if len(number)==n:
    for j in range(n):
        if num_to_check==number[j]:
            print("Number found at index {} and position {}".format(j,j+1))
            break
    else:
        print("Number not found")