#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
A = np.random.randint(2,size=(6))
B = np.random.randint(2,size=(6))
print(A)
print(B)
comparison = A==B
equal_arrays = comparison.all()
print(equal_arrays)


# In[ ]:




