data = ''
fp = open("file1.txt", "r") 
data = fp.read()
fp2 =  open ("file1_copy.txt" , "w") 
print(data.swapcase() , file = fp2)
fp2.close()