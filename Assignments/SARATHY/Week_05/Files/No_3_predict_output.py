# 3. Predict output of the following piece of code:
f =open('file','w')
f.write('line with some characters')
f.close()
f =open('file','r')
print(f.tell())
print(f.read(4))
print(f.tell())


# first tell() would tell the current cursor position before it is set to read
# f.read(4) would read the first four characters .if the whitespaces are there , it would take that also in account
# second f.tell() would tell the latest current position(i.e) as 4