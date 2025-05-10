#Shape A
rows = 7

for i in range(rows):
    for j in range((rows // 2) + 1):
        if (
            (j == 0 or j == rows // 2) and i != 0
            or (i == 0 and j != 0 and j != rows // 2)
            or i == rows // 2
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print()
