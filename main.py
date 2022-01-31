import matplotlib.pyplot as plt
import matplotlib
import random
import numpy as np
import math as m
import os

import time
start_time = time.time()


plt.ion()
coords = [[],[]]

inside = 0.0
outside = 0.0
    
# add a point to the graph
def addPoint(plot, new_point, c):
    old_off = plot.get_offsets()
    # make new array of points
    new_off = np.concatenate([old_off,np.array(new_point, ndmin=2)])
    plot.set_offsets(new_off)

    plot.axes.figure.canvas.draw_idle()

# create figure and circle
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
plt.title("Montecarlo Method of Calculating Pi") 
circle = plt.Circle((0,0),1.0,color='black', zorder=-1)
ax.set_aspect(1)
ax.add_patch(circle)

# create scatter plot of points
plot = plt.scatter(coords[0], coords[1], c='red', s=5, zorder=1)

POINTS = 1000

for i in range(POINTS):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    coords[0].append(x)
    coords[1].append(y)
    
    fig.canvas.draw()

    if x**2+y**2 < 1:
        inside+=1
        addPoint(plot, [x,y], 'white')
    else:
        outside+=1
        addPoint(plot, [x,y], 'black')
        
plt.pause(3)
print(4*inside/(outside+inside))


# CODE FOR WITHOUT GRAPH #

# inside = 0
# outside = 0
# for i in range(100000000):
#     x = random.uniform(-1,1)
#     y = random.uniform(-1,1)

#     # coords[0].append(x)
#     # coords[1].append(y)
    
#     if x**2+y**2 < 1:
#         inside+=1
#     else:
#         outside+=1

# print(4*inside/(outside+inside))
# print("--- %s seconds ---" % (time.time() - start_time))



