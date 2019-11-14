#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
#Funcion hombro izquierdo
def hombro(x, a, b):
    if x <= a:
      result = 1
    elif a < x < b:
      result = (b-x)/(b-a)
    elif x >= b:
      result = 0

    return result


res_hombro = []
numeros = np.arange(0, 10, 0.5)
for i in numeros:    
    res_hombro.append(hombro(i,3,5))
    
print(res_hombro)

