# Number Pattern | Part 2 | Python Pattern Programs

n = int(input("enter number of rows needed:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(n-j,end=" ")
    print()