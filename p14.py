# Print Numbers in Triangle Shape | Pattern Program | Python Tutorials

num = int(input("number of rows:"))

for i in range(num):
    k=111
    for j in range(num-i-1):
        print(format(" ","<5"),end="")
    
    k = k*(i+1)
    for j in range(i+1):
        print(format(k,"<5"),end="")
        k=k-111
    print()