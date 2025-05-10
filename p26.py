# Number Pattern | Part 3 | Python Pattern Programs

n = int(input("number of rows needed:"))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print(n-i,end=" ")
    print()