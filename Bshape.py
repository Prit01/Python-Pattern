#Shape B
'''
rows = 6


for i in range(rows):
    for j in range(5):
        if j == 0 or \
          (i == 0 and j < 4) or \
          (i == rows//2 and j < 4) or \
          (i == rows-1 and j < 4) or \
          (j == 4 and i != 0 and i != rows//2 and i != rows-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''

#------------------------------------------

for row in range(7):
   for col in range(5):
       if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
          print("*",end="")
       else:
          print(end=" ")
print()