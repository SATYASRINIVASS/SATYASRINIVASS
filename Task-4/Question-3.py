#!/usr/bin/env python
# coding: utf-8

# In[1]:


#creating given table
n=int(input('Enter the number of students : '))
a=[['Roll No','Name','Marks']]
for i in range(n):
    roll=input('Enter Roll No : ')
    studentname=input('Enter Student Name : ')
    marks=int(input('Enter Marks : '))
    a.append([roll,studentname,marks])
for i in range(len(a)):
    for j in range(len(a[i])):
        k=a[i][j]
        print(k,end='\t')
    print('\n')
h=int(input('Enter the row that should be printed : '))
for i in a[h]:
    print(i,end='\t')


# In[ ]:




