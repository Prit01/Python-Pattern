#Pyramid shape
def pyramid(rows):
    for i in range(rows):
        print(''*(rows-i-1)+'*'*(2*i+1))