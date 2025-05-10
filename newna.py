# New Name Pattern input anyone string
def get_letter_pattern():
    AtoZ = {}
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        AtoZ[ch] = [[" " for _ in range(6)] for _ in range(6)]

    # A
    for r in range(6):
        for c in range(6):
            if (r == 0 and c not in [0, 5]) or r == 3 or (c == 0 and r != 0) or (c == 5 and r != 0):
                AtoZ["A"][r][c] = "*"

    # B
    for r in range(6):
        for c in range(6):
            if c == 0 or ((r == 0 or r == 2 or r == 5) and c < 5) or (c == 5 and (r == 1 or r == 4)):
                AtoZ["B"][r][c] = "*"

    # C
    for r in range(6):
        for c in range(6):
            if r in [0, 5] and c > 0 or c == 0 and r not in [0, 5]:
                AtoZ["C"][r][c] = "*"

    # D
    for r in range(6):
        for c in range(6):
            if c == 0 or (r in [0, 5] and c < 5) or (c == 5 and r not in [0, 5]):
                AtoZ["D"][r][c] = "*"

    # E
    for r in range(6):
        for c in range(6):
            if r in [0, 2, 5] or c == 0:
                AtoZ["E"][r][c] = "*"

    # F
    for r in range(6):
        for c in range(6):
            if r in [0, 2] or c == 0:
                AtoZ["F"][r][c] = "*"

    # G
    for r in range(6):
        for c in range(6):
            if (r in [0, 5] and c > 0) or (c == 0 and r not in [0, 5]) or (r == 3 and c > 2) or (c == 5 and r in [3, 4]):
                AtoZ["G"][r][c] = "*"

    # H
    for r in range(6):
        for c in range(6):
            if c in [0, 5] or r == 3:
                AtoZ["H"][r][c] = "*"

    # I
    for r in range(6):
        for c in range(6):
            if r in [0, 5] or c == 2:
                AtoZ["I"][r][c] = "*"

    # J
    for r in range(6):
        for c in range(6):
            if r == 0 or (c == 2 and r != 5) or (r == 5 and c in [0, 1]):
                AtoZ["J"][r][c] = "*"

    # K
    for r in range(6):
        for c in range(6):
            if c == 0 or r + c == 5 or r - c == 0:
                AtoZ["K"][r][c] = "*"

    # L
    for r in range(6):
        for c in range(6):
            if c == 0 or r == 5:
                AtoZ["L"][r][c] = "*"

    # M
    for r in range(6):
        for c in range(6):
            if c in [0, 5] or (r == 1 and c in [1, 4]) or (r == 2 and c in [2, 3]):
                AtoZ["M"][r][c] = "*"

    # N
    for r in range(6):
        for c in range(6):
            if c in [0, 5] or r == c:
                AtoZ["N"][r][c] = "*"

    # O
    for r in range(6):
        for c in range(6):
            if (r in [0, 5] and c not in [0, 5]) or (c in [0, 5] and r not in [0, 5]):
                AtoZ["O"][r][c] = "*"

    # P
    for r in range(6):
        for c in range(6):
            if c == 0 or (r in [0, 2] and c < 5) or (c == 5 and r == 1):
                AtoZ["P"][r][c] = "*"

    # Q
    for r in range(6):
        for c in range(6):
            if (r in [0, 4] and c in [2, 3]) or (r == 1 and c in [1, 4]) or (r == 2 and c in [0, 5]) or (r == 3 and c in [1, 4]) or (r == 5 and c == 5):
                AtoZ["Q"][r][c] = "*"

    # R
    for r in range(6):
        for c in range(6):
            if c == 0 or (r in [0, 2] and c < 5) or (r == 1 and c == 5) or (r == 3 and c == 1) or (r == 4 and c == 2) or (r == 5 and c == 3):
                AtoZ["R"][r][c] = "*"

    # S
    for r in range(6):
        for c in range(6):
            if r in [0, 2, 5] or (r == 1 and c == 0) or (r == 4 and c == 5):
                AtoZ["S"][r][c] = "*"

    # T
    for r in range(6):
        for c in range(6):
            if r == 0 or c == 2:
                AtoZ["T"][r][c] = "*"

    # U
    for r in range(6):
        for c in range(6):
            if (c in [0, 5] and r != 5) or (r == 5 and c not in [0, 5]):
                AtoZ["U"][r][c] = "*"

    # V
    for r in range(5):
        for c in range(6):
            if (r == c and r < 3) or (r + c == 5 and r < 3) or (r == 3 and c in [1, 4]) or (r == 4 and c == 2):
                AtoZ["V"][r][c] = "*"

    # W
    for r in range(6):
        for c in range(6):
            if c in [0, 5] or (r == 4 and c in [1, 4]) or (r == 5 and c in [2, 3]):
                AtoZ["W"][r][c] = "*"

    # X
    for r in range(6):
        for c in range(6):
            if r == c or r + c == 5:
                AtoZ["X"][r][c] = "*"

    # Y
    for r in range(6):
        for c in range(6):
            if (r < 3 and (c == r or c == 5 - r)) or (r >= 3 and c == 2):
                AtoZ["Y"][r][c] = "*"

    # Z
    for r in range(6):
        for c in range(6):
            if r == 0 or r == 5 or r + c == 5:
                AtoZ["Z"][r][c] = "*"

    return AtoZ


def print_string(word):
    patterns = get_letter_pattern()
    word = word.upper()
    for row in range(6):
        for ch in word:
            if ch in patterns:
                print("".join(patterns[ch][row]), end="   ")
            else:
                print(" " * 6, end="   ")
        print()


# 🖊️ Take input from user
user_input = input("Enter a word to print in star pattern: ")
print_string(user_input)
