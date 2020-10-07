#10. Update the above program to count the number of palindromes present in the file.

with open('palindrome.txt','r') as f:
	words = f.read().split()
	print(words)
	pali_words=[]
	for i in words:
		if i[:]==i[::-1]:
			pali_words.append(i)
		
	print(pali_words)
	