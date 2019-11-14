#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
#Funcion sigmoidal
def sigmoidal(x, a, m, b):
    if x <= a:
      result = 0
    elif a < x <= m:
      result = 2 * ((x-a)/(b-a))**2
    elif m < x < b:
      result = 1 - 2 * ((x-b)/(b-a))**2
    elif x >= b:
      result = 1

    return result

res_sigmoidal = []
numeros = np.arange(0, 10, 0.5)
for i in numeros:    
    res_sigmoidal.append(sigmoidal(i,3,5,7))
    
print(res_sigmoidal)

