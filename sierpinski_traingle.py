# -*- coding: utf-8 -*-
"""Sierpinski Traingle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l-1PVwIKoI1cJe5xcd_05vy8ZCN8pUjF
"""

# Sirpienski Pseudocode

# The Sierpiński triangle:
#  A fractal attractive fixed set with the overall shape of an equilateral triangle
#  subdivided recursively into smaller equilateral triangles.

import matplotlib.pyplot as plt
import random
import numpy as np

N = 10000
x = np.zeros(N)
y = np.zeros(N)
for i in range(1, N):
  k    = random.randint(1,3)
  x[i] = x[i-1]/2 + k-1
  y[i] = y[i-1]/2
  if k==2:
    y[i] = y[i]+2 
  
plt.plot(x,y,'k.', markersize=1)

plt.title("Sierpinski Traingle",fontsize=20)
plt.show()