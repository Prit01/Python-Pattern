# Debugging The Pascal's Triangle - Python Pattern Program | Working

n = int(input("enter the row number:"))
list1 = []
for i in range(n):
    temp_list=[]
    for j in range(i+1):
        if j==0 or j==i:
            temp_list.append(1)
        else:
            temp_list.append(list1[i-1][j-1] + list1[i-1][j])
    list1.append(temp_list)

for i in range(n):
    for j in range(n-i-1):
        print(format(" ","<2"),end="")
    for j in range(i+1):
        print(format(list1[i][j],"<4"),end="")
    print()