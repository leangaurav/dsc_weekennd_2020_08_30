import sys
sum1 = 0
sum2 = ''
a = sys.argv
print(len(a))
for i in a[1:] :
    try:
        if int(i) >= 0:
            sum1 = sum1+ int(i) 
        elif int(i) < 0:
            pass
    except:
        if i.isalpha:
            sum2= sum2 + i
        else:
            pass

print(sum1)
print(sum2)
