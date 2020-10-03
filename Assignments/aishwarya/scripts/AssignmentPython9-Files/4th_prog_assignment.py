data = ''
fp = open("alpha.txt", "r") 
data = fp.read()
fp2 =  open ("alpha_copy.txt" , "w") 
print(data , file = fp2)
fp2.close()