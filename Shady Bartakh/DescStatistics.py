import numpy as np
from collections import Counter
from statistics import mode

lst = [1,3,55,66,3,66,3,9]

# Without libraries
mean=0
for element in lst:
    mean+=element
    
mean=mean/len(lst)
print(f'manual calc. of mean: {mean}')

# using library
mean=np.mean(lst)
print(f'Library mean: {mean}')

# Without libraries
lst.sort()

if len(lst)%2==0:  # even items
    med1=lst[len(lst)//2 -1]
    med2=lst[len(lst)//2]
    median=(med1+med2)/2
else:
    median=lst[len(lst)//2]
print(f'manual calc. of median: {median}')

# using library
median=np.median(lst)
print(f'Library median: {median}')

# Without libraries
mode1  = [k for k,v in Counter(lst).items() if v==max(Counter(lst).values())]
print(f'manual calc. of mode: {mode1}')

# using library
mode2=mode(lst)
print(f'Library mode: {mode2}')

# Without libraries
var_i = 0  # initial value for variance calculation
for i in lst:
    var_i += pow(i-mean,2)
var = var_i/len(lst)
print(f'manual calc. of variance: {var}')

# using library
var=np.var(lst)
print(f'Library variance: {var}')