#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to get the Fibonacci series between 0 to 50

# In[1]:



start=int(input("enter start number:"))
end=int(input("enter end number:"))
n1,n2=0,1
sum=0
for i in range(0,10):
    print(sum,end=" ")
    n1=n2
    n2=sum
    sum=n1+n2


# In[ ]:




