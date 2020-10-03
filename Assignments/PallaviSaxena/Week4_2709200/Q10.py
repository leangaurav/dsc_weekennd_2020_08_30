import sys
c = 0
with open(sys.argv[1], "r") as f:
    words = f.read().split()
    for w in words:
        if w[::-1] in words and len(w) != 1:
            c += 1
            print(w)
print("Number of palindromes are: ", c)
