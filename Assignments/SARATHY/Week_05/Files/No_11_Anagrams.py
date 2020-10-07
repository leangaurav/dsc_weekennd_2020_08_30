import sys
anagram_list={}
occurence=0
with open(sys.argv[0],'r') as f1:	
	sorted_strings = [('').join(sorted(w)) for w in f1.read().split()]
	for i in sorted_strings:
		if i in anagram_list.keys():
			anagram_list[i]+=1
		else:
			anagram_list[i]=1
	print(anagram_list)
with open('anagram.txt','w') as f2:
	f2.write(str(anagram_list))
for i,j in anagram_list.items():
	if anagram_list[i]>1:
		occurence+=1
print("The total no of anagrams are : " ,occurence)
	