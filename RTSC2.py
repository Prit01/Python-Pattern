# Python Pattern Programs - Printing Numbers in Right Triangle Shape 2 | Column wise
n = int(input("enter the number of rows:"))
for i in range(n):
    for j in range(i+1):
        x = 0
        for k in range(j):
            x = x+n-k
        if j%2==0:
            print(x+i-j+1,end=" ")
        else:
            print(x+n-i,end=" ")
    print()