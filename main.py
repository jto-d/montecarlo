import matplotlib.pyplot as plt
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
    

# fig = plt.figure(figsize=(10,10))
# ax = fig.add_subplot(111)
# plt.title("Montecarlo Method of Calculating Pi") 
# circle = plt.Circle((0,0),1.0,color='black', zorder=-1)
# ax.set_aspect(1)
# ax.add_patch(circle)

# for i in range(100000):
#     x = random.uniform(-1,1)
#     y = random.uniform(-1,1)

#     coords[0].append(x)
#     coords[1].append(y)
    
#     if x**2+y**2 < 1:
#         inside+=1
#         # plt.scatter(coords[0], coords[1], c='white', zorder=1)
#     else:
#         outside+=1

#     # plt.scatter(coords[0], coords[1], c='red', s=5, zorder=1)
#     # fig.canvas.draw()
#     # fig.canvas.flush_events()


# plt.scatter(coords[0], coords[1], c='red', s=1, zorder=1)
# print(4*inside/(outside+inside))
# fig.canvas.draw()
# plt.pause(3)


inside = 0
outside = 0
for i in range(100000000):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    # coords[0].append(x)
    # coords[1].append(y)
    
    if x**2+y**2 < 1:
        inside+=1
    else:
        outside+=1

print(4*inside/(outside+inside))
print("--- %s seconds ---" % (time.time() - start_time))



