#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
#Funcion Hombro derecho o saturacion
def saturacion(x, a, b):
    if x <= a:
      result = 0
    elif a < x < b:
      result = (x-a)/(b-a)
    elif x >= b:
      result = 1
    
    return result

resultado_saturacion = []
numeros = np.arange(0, 10, 0.5)
for i in numeros:    
    resultado_saturacion.append(saturacion(i,3,5))
    
print(resultado_saturacion)

