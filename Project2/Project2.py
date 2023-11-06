#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
import matplotlib.pyplot as plt


x = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
print(x)
n = 0.001
w = n* np.random.random(size=(3, 3))
print(w)

y = np.zeros((4,3))
e = np.zeros((4,3))
e_mean = np.zeros((40,3))

d = np.array([[0,0,0],[0,1,1],[0,1,1],[1,1,0]])

for i in range(0,40):
    y = np.dot(x,w)
    for j in range(0,4):
        for k in range(0,3):
            if y[j,k]>= 0 :
                y[j,k] = 1
            if y[j,k]<0:
                y[j,k] = 0
    x1 = np.transpose(x)
    e = d - y
    w = w + n*np.dot(x1,e)
    # calculating error for three gates: or, and, xor
    e_mean[i, 0] = abs(np.mean(e[0:4 , 0]))
    e_mean[i, 1] = abs(np.mean(e[0:4 , 1]))
    e_mean[i, 2] = abs(np.mean(e[0:4 , 2]))

# y after learning in neural network    
print(y)
# printing error for OR,AND, XOR gates
print(e_mean)

plt.figure(figsize=(20,20))
plt.subplot(3,1,1)
plt.title('AND')
plt.plot(e_mean[0:40 , 0])

plt.subplot(3,1,2)
plt.title('OR')
plt.plot(e_mean[0:40 , 1])

plt.subplot(3,1,3)
plt.title('XOR')
plt.plot(e_mean[0:40 , 2])

plt.show()


# In[ ]:





# In[ ]:




