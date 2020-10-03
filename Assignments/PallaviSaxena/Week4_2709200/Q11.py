import sys
count_dict = {}
total = 0
with open(sys.argv[1], "r") as f:
    sorted_words = [''.join(sorted(w)) for w in f.read().split()]
    for w in sorted_words:
        if w in count_dict.keys():
            count_dict[w] += 1
        else:
            count_dict[w] = 1 
for c in count_dict.keys():
    if count_dict[c] > 1:
        total += 1
        
print("Number of anargrams are: ", total)
print("List of anargrams are: ", count_dict)
