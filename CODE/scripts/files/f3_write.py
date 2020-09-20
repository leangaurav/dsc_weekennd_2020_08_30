# open a file
f = open("temp_a.txt", "a") # append: add some data to a file. and create it
print(f)
f.write("First  line" + str(100))
f.write("Same line")
f.write("\n Next line")
f.close()
