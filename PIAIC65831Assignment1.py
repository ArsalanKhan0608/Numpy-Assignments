#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[1]:


import numpy as np


# 2. Create a null vector of size 10 

# In[27]:


null_vector = np.zeros(10)


# 3. Create a vector with values ranging from 10 to 49

# In[28]:


arr = np.arange(10,49)


# 4. Find the shape of previous array in question 3

# In[29]:


arr = np.arange(10,49)
np.shape(arr)


# 5. Print the type of the previous array in question 3

# In[30]:


arr = np.arange(10,49)
arr.dtype


# 6. Print the numpy version and the configuration
# 

# In[31]:


np.__version__


# In[32]:


np.show_config()


# 7. Print the dimension of the array in question 3
# 

# In[33]:


arr = np.arange(10,49)
arr.ndim


# 8. Create a boolean array with all the True values

# In[34]:


ar =np.ones(10, dtype =bool )
ar


# 9. Create a two dimensional array
# 
# 
# 

# In[35]:


b = np.arange(12).reshape(4,3)
b


# 10. Create a three dimensional array
# 
# 

# In[36]:


c = np.arange(24).reshape(2,3,4)
c


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[37]:


arr = np.arange(1,10)
arr


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[38]:


arr = np.arange(1,10)
arr[::-1]


# 13. Create a 3x3 identity matrix

# In[39]:


x =  np.arange(2, 11).reshape(3,3)
print(x)


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[40]:


arr = np.array([1, 2, 3, 4, 5])
arr.astype(float)


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[41]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
arr1 * arr2


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[42]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])

comparison = arr1 == arr2        
equal_arrays = comparison.all()    # all() TO CHECK IF TWO ARRAYS ARE EQUIVALENT
equal_arrays


# 17. Extract all odd numbers from arr with values(0-9)

# In[43]:


arry1=np.arange(9)
a = arry1[arry1%2!=0] 
print(a) 


# 18. Replace all odd numbers to -1 from previous array

# In[44]:


arry1=np.arange(9)
arry1[arry1%2!=0]= -1 
print(arry1)


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[45]:


arr = np.arange(10)
arr[5]=12
arr[6]=12
arr[7]=12
arr[8]=12
arr
    
# 20. Create a 2d array with 1 on the border and 0 inside

# In[46]:


b = np.arange(12).reshape(4,3) 
b[0,0]=1
b[0,2]=1
b[1,0]=1
b[1,2]=1
b[2,0]=1
b[2,2]=1
b[3,0]=1
b[3,2]=1
b[3,1]=1
b[1,1]=0
b[2,1]=0
b


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[47]:


arr2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
arr2d[1,1]=12
arr2d


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[48]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[1,0,0]=64
arr3d[1,0,1]=64
arr3d[1,0,2]=64
arr3d[1,1,0]=64
arr3d[1,1,1]=64
arr3d[1,1,2]=64
print(arr3d)


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[49]:


b = np.arange(9).reshape(3,3)
b[0]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[50]:


arr=np.arange(0,9)
arr.reshape(3,3)
arr[1]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[51]:


arr = np.arange(9).reshape(3,3)
arr


# In[52]:


arr[0]


# In[53]:


arr[1]


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[54]:


arr = np.random.randint(100,size=(10,10))
arr


# In[55]:


print(np.min(arr))
print(np.max(arr))


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[56]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
r = np.intersect1d(a,b)
r


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[57]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
r = np.intersect1d(a,b)
print(r)


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[58]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
data[names != "Will"]


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[59]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
print(data[names !="Will"])
print(data[names !="Joe"])


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[60]:


arr = np.random.randn(1,15).reshape(5,3)
arr


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[61]:


dara = np.random.randn(1,16).reshape(2,2,4)


# 33. Swap axes of the array you created in Question 32

# In[62]:


dara = np.random.randn(1,16).reshape(2,2,4)
data.T


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[63]:


r = np.arange(10)
r = np.sqrt(r)
np.where(r<0.5,0,r)


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[64]:


a = np.random.randint(12)
b = np.random.randint(12)
np.maximum(a,b)


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[65]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
names 


# In[66]:


names = set (names)
names


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[67]:


a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
result = np.setdiff1d(a, b)
print(result)


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[68]:


saArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
saArray[2:]= ([[10,10,10]])
saArray


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[69]:


x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
np.dot(x,y)


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[70]:


A = np.random.randint(20, size=(4,4))
A


# In[71]:


np.sum(A)

