# open a file
f = open("temp_a.txt", "a") # append: add some data to a file. and create it
print(f)

print("Hello", "abc", 10, 30, file=f)
print("Hello Next line", file=f)
f.close()
