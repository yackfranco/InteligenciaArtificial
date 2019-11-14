#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
#Funcion triangular

def triangular(x, a, m, b):

    if x <= a or x >= b:
      result = 0
    elif a < x <= m:
      result = (x-a)/(m-a)
    elif m < x < b:
      result = (b-x)/(b-m)

    return result


res_triangular = []
numeros = np.arange(0, 10, 0.5)
for i in numeros:    
    res_triangular.append(triangular(i,3,5,7))
    
print(res_triangular)

