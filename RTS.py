# Printing Numbers in Right Triangle Shape
n = input("enter the number of rows:")
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(col,)
    print()