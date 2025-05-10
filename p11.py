# Python Pattern Programs - Printing Stars '*' and "A" in Right Angle Triangle Shape | Star Pattern

n = int(input("enter the number of rows:"))
for i in range(n):
    count=0
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
        if count<i:
            print("A",end="")
            count=count+1
    print()