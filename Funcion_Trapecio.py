#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
#Funcion trapecio
def trapecio(x, a, b, c, d):

    if x <= a or x >= d:
      result = 0
    elif a < x < b:
      result = (x-a) / (b-a)
    elif b <= x <= c:
      result = 1
    elif c < x < d:
      result = (d-x) / (d-c)
    
    return result

res_trapecio = []
numeros = np.arange(0, 10, 0.5)
for i in numeros:    
    res_trapecio.append(trapecio(i,3,5,7,9))
    
print(res_trapecio)

