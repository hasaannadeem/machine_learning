#!/usr/bin/env python
# coding: utf-8

# ![](images/la.jpg)

# ### Load in NumPy (remember to pip install numpy first)

# In[14]:


import numpy as np


# ### The Basics

# In[20]:


arr = np.array([[1,4,7],[2,3,5],[2,3,5],[2,3,5]])
print(arr)


# In[35]:


# create an integer array
a = np.array([1,2,3,4,5])
print(a)


# In[28]:


# create a float array
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0],[6.0,5.0,4.0]])
print(b)


# In[26]:


# Get Dimension
arr.ndim


# In[29]:


# Get Shape
b.shape


# In[30]:


# Get Type
a.dtype


# In[31]:


# Get total size
a.nbytes


# In[36]:


# Get number of elements
a.size


# ### Accessing/Changing specific elements, rows, columns, etc

# In[38]:


arr = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(arr)


# In[42]:


# Get a specific element [row, column]
arr[1,6]


# In[46]:


# Get a specific row 
arr[1, :]


# In[50]:


# Get a specific column
arr[:, 4]


# In[56]:


arr[0,1:-1:3]


# In[58]:


# Getting a little more fancy [startindex:endindex:stepsize]
a[0, 1:-1:1]


# In[24]:


a[1,5] = 20

a[:,2] = [1,2]
print(a)


# *3-d example

# ### Initializing Different Types of Arrays

# In[40]:


# All 0s matrix
np.zeros((2,3))


# In[42]:


# All 1s matrix
np.ones((4,2,2), dtype='int32')


# In[44]:


# Any other number
np.full((2,2), 99)


# In[49]:


# Any other number (full_like)
np.full_like(a, 4)


# In[56]:


# Random decimal numbers
np.random.rand(4,2)


# In[73]:


# Random Integer values
np.random.randint(-4,8, size=(3,3))


# In[61]:


# The identity matrix
np.identity(3)


# In[82]:


# Repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print(r1)


# In[12]:


output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

# output[1:-1,1:-1] = z
# print(output)


# ##### Be careful when copying arrays!!!

# In[62]:


# Copy an Array
a = np.array([1,2,3])
b = a.copy()
b[0] = 100

print(b)


# ### Mathematics

# In[63]:


a = np.array([1,2,3,4])
print(a)


# In[ ]:


# array to array addition


# In[64]:


a + 2


# In[65]:


a - 2


# In[66]:


a * 2


# In[67]:


a / 2


# In[68]:


b = np.array([1,0,1,0])
a + b


# In[69]:


a ** 2


# In[70]:


# Take the sin
np.cos(a)


# In[71]:


np.sin(a)


# In[72]:


np.tanh(a)


# In[73]:


np.exp(a)


# In[74]:


np.log(a)


# ##### Lists and Arrays

# In[81]:


# create a list
lst = [1,2,3,4,5,6]
print(type(lst))


# In[84]:


# contact a list
newlst = [7,8,9]
lst+newlst


# In[ ]:


# append method


# In[ ]:


# adding lists
lst + lst


# In[ ]:


# Scalar Multiplication
lst * 4


# ##### Linear Algebra

# In[127]:


a = np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

np.matmul(a,b)


# In[132]:


# Find the determinant
c = np.identity(3)
np.linalg.det(c)


# In[133]:


## Reference docs (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
# Etc...


# ##### Statistics

# In[85]:


stats = np.array([[1,2,3],[4,5,6]])
stats


# In[86]:


np.min(stats)


# In[88]:


np.max(stats, axis=1)


# In[89]:


np.sum(stats, axis=0)


# ### Reorganizing Arrays

# In[151]:


before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((2,3))
print(after)


# In[158]:


# Vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1,v2,v1,v2])


# In[164]:


# Horizontal  stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

np.hstack((h1,h2))


# ### Miscellaneous
# ##### Load Data from File

# In[179]:


filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)


# ##### Boolean Masking and Advanced Indexing

# In[196]:


(~((filedata > 50) & (filedata < 100)))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




