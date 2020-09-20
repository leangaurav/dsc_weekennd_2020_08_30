# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import string
import sys


# %%
sum = 0
for i in range(1, len(sys.argv)):
    if(str.isnumeric(sys.argv[i])):
        sum = sum + int(sys.argv[i])
    else:    
        list = sys.argv[i].split('.')
        if len(list)>0 and str.isnumeric(list[0]) and str.isnumeric(list[1]):
            sum = sum + int(list[0])

print("Sum is", sum)






# %%
