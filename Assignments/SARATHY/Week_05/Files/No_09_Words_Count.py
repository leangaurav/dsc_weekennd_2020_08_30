# 9. WAP to count the number of words in a
with open('occurence1.txt','r') as f:
	words = f.read().split()
	print(len(words))
	