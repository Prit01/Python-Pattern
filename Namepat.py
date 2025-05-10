# Python Pattern Programs - Printing Names Using Stars "*" | Star Pattern
'''
str1 = "NO"
print_N = [[" " for i in range(6)] for j in range(6)]
print_O = [[" " for i in range(6)] for j in range(6)]

#code for N
for row in range(6):
    for col in range(6):
        if col==0 or col==5 or row==col:
            print_N[row][col]="*"

#code for O
for row in range(6):
    for col in range(6):
        if ((row==0 or row==5) and (col!=0 and col!=5)) or (col==0 or col==5) and ((row!=0 and row!=5)):
            print_O[row][col]= "*"

for i in range(6):
    for j in range(6):
        print(print_N[i][j],end="")
    print(end="   ")
    for j in range(6):
        print(print_O[i][j],end="")
    print()
'''

str1 = "PRIYANSHU"
patterns = {}

# Initialize 6x6 grid for each letter
for ch in str1:
    patterns[ch] = [[" " for i in range(6)] for j in range(6)]

# Letter P
for row in range(6):
    for col in range(6):
        if col == 0 or (row == 0 or row == 2) and col < 5 or (row == 1 and col == 5):
            patterns["P"][row][col] = "*"

# Letter R
for row in range(6):
    for col in range(6):
        if col == 0 or (row == 0 or row == 2) and col < 5 or (row == 1 and col == 5) or (row == 3 and col == 1) or (row == 4 and col == 2) or (row == 5 and col == 3):
            patterns["R"][row][col] = "*"

# Letter I
for row in range(6):
    for col in range(6):
        if row == 0 or row == 5 or col == 2:
            patterns["I"][row][col] = "*"

# Letter Y
for row in range(6):
    for col in range(6):
        if (row < 3 and (col == row or col == 5 - row)) or (row >= 3 and col == 2):
            patterns["Y"][row][col] = "*"

# Letter A
for row in range(6):
    for col in range(6):
        if row == 0 and col not in [0, 5] or row == 3 or col == 0 and row != 0 or col == 5 and row != 0:
            patterns["A"][row][col] = "*"

# Letter N
for row in range(6):
    for col in range(6):
        if col == 0 or col == 5 or row == col:
            patterns["N"][row][col] = "*"

# Letter S
for row in range(6):
    for col in range(6):
        if row == 0 or row == 2 or row == 5 or (row == 1 and col == 0) or (row == 3 and col == 5) or (row == 4 and col == 0):
            patterns["S"][row][col] = "*"

# Letter H
for row in range(6):
    for col in range(6):
        if col == 0 or col == 5 or row == 3:
            patterns["H"][row][col] = "*"

# Letter U
for row in range(6):
    for col in range(6):
        if (col == 0 or col == 5) and row != 5 or row == 5 and col not in [0, 5]:
            patterns["U"][row][col] = "*"

# Print all letters row by row
for row in range(6):
    for ch in str1:
        for col in range(6):
            print(patterns[ch][row][col], end="")
        print(end="   ")  # Space between letters
    print()
