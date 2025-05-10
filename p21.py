# Alphabet Pattern - Printing Alphabet in Right Triangle Shape | Python Programs

n = int(input("Enter the number of rows:"))
k = ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()
