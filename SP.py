# Python Pattern Programs - Printing Stars '*' in Different Shapes | Star Pattern

num = int(input("enter the number of rows:"))
for i in range(1,num+1):
    print("* "*i)
for i in range(num,0,-1):
    print("* "*i)