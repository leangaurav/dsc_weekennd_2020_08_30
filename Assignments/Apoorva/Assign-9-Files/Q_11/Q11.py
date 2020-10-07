# 11. Update the program again to count and print 
# number of anagrams in the file.

# Anagrams => rearrange letters of a word to form a another word
# Checking if n words have same letters

c = 0
with open('readfile.txt','r') as f_read:
	content = f_read.read().split()
	sorted_words = [ ''.join(sorted(word)) for word in content]
	d ={}
	for word1 in sorted_words:
		if word1 in sorted_words:
		   d[word1] = d.get(word1,0) + 1

			
	for (key,value) in d.items():
		d[key] = value - 1
	print('count of Anagrams found for each word: ',d)
		
