import time
from datetime import datetime

f = open("file.csv", "w")
for i in range(10):
    print(i,datetime.now(), sep=',', file=f)
    print(i)
    time.sleep(1)

f.close()