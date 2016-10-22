# -*- coding: utf-8 -*-
"""
Jinxiu Liu
This is a temporary script file.

"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(1000)
y = np.random.rand(1000)
colors = np.random.rand(1000)
plt.scatter(x,y,c=colors)
plt.title('Random Candy points')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

