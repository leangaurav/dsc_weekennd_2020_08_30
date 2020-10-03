import sys
count_dict = {}
with open(sys.argv[1], "r") as f:
    for c in f.read():
        if c in count_dict.keys():
            count_dict[c] += 1
        else:
            count_dict[c] = 1
print(count_dict)
