from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# multiple  line chart in same window as tiles
# subplot: subplot(r, c, idx) (2,3,1) => split window into a matrix  2x3 and  we are plotting graph-1
s = pd.Series(range(10,100,10))
s1 =  s*2
s2 =  s**2
s3 =  s**3

plt.subplot(2,2,1)
plt.plot(s.index, s.values)

plt.subplot(2,2,2)
plt.plot(s1.index, s1.values)

plt.subplot(2,2,3)
plt.plot(s2.index, s2.values)

plt.subplot(2,2,4)
plt.plot(s3.index, s3.values)
plt.show()