#R shape pattern
'''
for row in range(7):
    for col in range(5):
        if col==0 or (col==4 and(row!=0 and row!=3)) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end="")
    print()

'''


n = 7
for i in range(n):
    for j in range(n):
        # Vertical line on the left
        if j == 0:
            print("*", end="")
        # Top horizontal line
        elif i == 0 and j < n - 1:
            print("*", end="")
        # Middle horizontal line
        elif i == n//2 and j < n - 1:
            print("*", end="")
        # Right vertical line of the upper part
        elif j == n - 1 and i < n//2 and i != 0:
            print("*", end="")
        # Diagonal line for the leg of R
        elif i - j == n//2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
