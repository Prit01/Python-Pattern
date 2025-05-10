# Python Pattern Program - Diamond Number Pattern

n = int(input("how many rows you want?"))
for i in range(n):
    k = i+1
    for j in range(n-i-1):
        print(" ",end="   ")
    for j in range(i+1):
        print(k,end=" ")
        k = k-1
    if i>0:
        for j in range(i-1):
            print(" ",end=" ")
        for j in range(i+1):
            k = k+1
            print(k,end=" ")
    print()

for i in range(1,n):
    k=n-1
    for j in range(i):
        print(" ",end="   ")
    for j in range(i+1):
        print(k,end=" ")
        k=k-1
    if i<(n-1):
        for j in range(n-i-2 ):
            print(" ",end=" ")
        for j in range(i+1):
            k=k+1
            print(k,end=" ")
    print()