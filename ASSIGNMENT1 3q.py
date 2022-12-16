#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to count the number of even and odd numbers from a series of numbers.

# In[3]:


numbers=eval(input("enter numbers"))
even_count, odd_count = 0, 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1 
print("Even number count is: ", even_count)
print("Odd number count is : ", odd_count)


# In[ ]:





# In[ ]:




