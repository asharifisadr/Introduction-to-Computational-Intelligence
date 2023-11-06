#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

x = np.random.randint(0, 20, size=(101, 3))
x[0:100, 0] = x[0:100, 2]
print(x)

n = 0.001
w = n* np.random.random(size=(3, 3))
print(w)

y = np.zeros((101,3))
e = np.zeros((100,3))
e_mean = np.zeros((100,1))

x1 = np.zeros((1,3))

for i in range (0,80):
    y[i:i+1 , 0:3] = np.dot(x[i:i+1, 0:3],w) 
    e[i:i+1 , 0:3] = (x[i:i+1 , 0:3] - y[i:i+1 , 0:3])
    e_mean[i:i+1 , 0:1] = np.mean(e[i:i+1 , 0:3]) 
    x1 = np.transpose(x[i:i+1 , 0:3])
    w = w + 0.001*(np.dot(x1,e[i:i+1, 0:3]))

print(w)

 
for i in range (80,100):
    y[i:i+1 , 0:3] = np.dot(x[i:i+1, 0:3],w) 
    e[i:i+1 , 0:3] = (x[i:i+1 , 0:3] - y[i:i+1 , 0:3])

      


fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter3d(x=x[0:80 , 0], y=x[0:80 , 1], z=x[0:80 , 2], mode='markers',   marker=dict(symbol="circle", size=4)))
fig.add_trace(go.Scatter3d(x=y[0:80 , 0], y=y[0:80 , 1], z=y[0:80 , 2], mode='markers',   marker=dict(symbol="cross", size=5)))

fig.show()

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter3d(x=x[80:100 , 0], y=x[80:100 , 1], z=x[80:100 , 2], mode='markers',   marker=dict(symbol="circle", size=4)))
fig.add_trace(go.Scatter3d(x=y[80:100 , 0], y=y[80:100 , 1], z=y[80:100 , 2], mode='markers',   marker=dict(symbol="cross", size=6)))

x[100:101 , 0:3] = [5,20,32]
print(x[100:101 , 0:3])
y[100:101 , 0:3] = np.dot(x[100:101 , 0:3],w) 
fig.add_trace(go.Scatter3d(x=x[100:101 , 0], y=x[100:101 , 1], z=x[100:101 , 2], mode='markers',   marker=dict(symbol="diamond", size=6)))
fig.add_trace(go.Scatter3d(x=y[100:101 , 0], y=y[100:101 , 1], z=y[100:101 , 2], mode='markers',   marker=dict(symbol="diamond", size=6)))

fig.show()


t = np.linspace(0,100,100)
plt.plot(t,e_mean)
plt.show()


# In[ ]:





# In[ ]:




