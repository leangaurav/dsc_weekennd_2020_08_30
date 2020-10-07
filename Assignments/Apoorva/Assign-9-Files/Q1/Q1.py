#1. Write a program in python that stores alphabets from a to z in a text file.
import string

f = open('Q1.txt','w')
print("Entering lowercase Alphabets in Q1.txt")
f.write(string.ascii_lowercase)
f.close()