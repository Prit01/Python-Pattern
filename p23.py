# String Pattern | Python Pattern Programs

str1 = input("enter string:")
length = len(str1)
for i in range(length):
    for j in range(length-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(str1[i],end=" ")
    print()
