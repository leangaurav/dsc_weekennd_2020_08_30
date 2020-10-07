#2. Write a program to read itself and print on the screen (Use Command Line Arguments).

import sys
f_read = open(sys.argv[0],'r')
f_write = open ('Q2.txt','w')

f_write.write(f_read.read())

f_write.close()
f_read.close()


"""import sys
with open(sys.argv[0], "r") as f1:
    with open(sys.argv[0] + "copy", "w") as f2:
        f2.write(f1.read())"""