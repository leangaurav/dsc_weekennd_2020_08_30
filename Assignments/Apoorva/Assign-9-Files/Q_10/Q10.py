# 10. Update the above program to count the number of palindromes present in the file.


def is_palin(word):
	check = 0
	if word == word[::-1]:
			return True
	#return False
		


with open('readfile.txt','r') as f_read:
	content = f_read.read().split()
	palin=0
	for word in content:
		if (is_palin(word)):
			palin+=1

print("Number of words: ",len(content))
print("Number of palindrome words: ",palin)