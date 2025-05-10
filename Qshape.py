#Q  shape Pattern
'''
for row in range(8):
    for col in range(5):
        if ((col==0 or col==4) and (row>0 and row<6)) or ((row==0 and row==6) and (col>0 and col<4)) or (row==5 and col==1) or (row==7 and col==3):
            print("*",end="")
        else:
            print(end=" ")
    print()

    '''

# --------------------------------------

rows = 7
cols = 9

for i in range(rows):
    for j in range(cols):
        if (
            (i == 0 and 2 <= j <= 6) or  # Top curve
            (i == 6 and j == 7) or      # Tail of Q
            (j == 1 and 1 <= i <= 5) or # Left vertical
            (j == 7 and 1 <= i <= 4) or # Right vertical
            (i == 5 and j == 5) or      # Inner slash
            (i == 6 and j == 8)         # Dot at bottom-right
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print()
