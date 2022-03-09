#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


#1. adding two numpy arrays
import numpy as np
from numpy import *
a_1= int(input("enter the number of elements you want  : "))
p= zeros(a_1, dtype=int)
for i in range(len(p)):
    x=int(input("enter the elements: "))
    p[i] = x
a_2=int(input("enter the number of elements you want : ")) 
q= zeros(a_2, dtype=int)
for i in range(len(q)):
    y=int(input("enter the elements: "))
    q[i] = y
print("\nFirst array: ",p)
print("\nSecond array: ",q)
r=np.add(p,q) # using add function
print("\nSum of the  arrays : ",r)


# In[ ]:


# 4. array datatype conversion

import numpy as np
from numpy import *
num= int(input("enter the number of elements you want: "))
arr= zeros(num, dtype=int)
for i in range(len(arr)):
    x=int(input("enter the elements: "))
    arr[i] = x
print(arr) 
print(arr.dtype)
arr = arr.astype('float64')
print(arr)
print(arr.dtype)


# In[ ]:


# In[ ]:




