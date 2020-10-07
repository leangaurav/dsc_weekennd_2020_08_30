f = open('file' , 'w')
f.write('linewith some character')
f.close()

f = open('file' ,'r')
print(f.tell())
print(f.read(4))
print(f.tell())