# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:08:25 2022

@author: et24233
"""

import matplotlib.pyplot as plt
import numpy as np

#Wafer Parameters#
diameter = 4
dieSizeX = 2
dieSizeY = 2


###### Defining Center Points ######


#Creating arrays for the die centers x and y#    
dieCenterPosX = (np.arange((dieSizeX/2), (diameter/2), (dieSizeX))) 
dieCenterNegX = dieCenterPosX*-1 
dieCenterX = np.concatenate((dieCenterNegX, dieCenterPosX), axis=0)
dieCenterX.sort()

dieCenterPosY =  (np.arange((dieSizeY/2), (diameter/2), (dieSizeY)))
dieCenterNegY = dieCenterPosY*-1
dieCenterY = np.concatenate((dieCenterNegY, dieCenterPosY), axis=0)
dieCenterY.sort()

#Creating a class to define center points#
class Dice:
    def __init__(self, center, V1,V2,V3,V4):
        self.center = center
        self.V1 = V1
        self.V2 = V2
        self.V3 = V3
        self.V4 = V4
        
        
#Printing coordinates of center points of dice using for loops#     
d1 = []  
print("Die Centers:")  
for i in range(0,len(dieCenterX)):
    for j in range(0,len(dieCenterY)):
        dieCenter = np.array(([dieCenterX[i], dieCenterY[j]]))
        print(dieCenter)
        
print("\n" + "V1s: ")       
for k in range(0,len(dieCenterX)):
    for l in range(0,len(dieCenterY)):        
        v1X = dieCenterX+(dieSizeX/2)
        v1Y = dieCenterY+(dieSizeY/2)
        v1 = np.array(([v1X[k], v1Y[l]]))
        print(v1)
        
print("\n" + "V2s: ")       
for m in range(0,len(dieCenterX)):
    for n in range(0,len(dieCenterY)):        
        v2X = -v1X
        v2Y = v1Y
        v2 = np.array(([v2X[m], v2Y[n]]))
        print(v2)
        
print("\n" + "V3s: ")       
for o in range(0,len(dieCenterX)):
    for p in range(0,len(dieCenterY)):        
        v3X = -v1X
        v3Y = -v1Y
        v3 = np.array(([v3X[o], v3Y[p]]))
        print(v3)
        
print("\n" + "V4s: ")       
for q in range(0,len(dieCenterX)):
    for r in range(0,len(dieCenterY)): 
        v4X = v1X
        v4Y = -v1Y
        v4 = np.array(([v4X[q], v4Y[r]]))
        print(v4)
        
        # if V1,V2,V3,V4 are within the wafer radius then append
        #d1.append(Dice(dieCenter, v1, v2, v3, v4))
        
    
            
        
"""       
###### Generating the Plot ######
x = np.arange(-diameter, diameter, dieSizeX/2)
y = np.arange(-diameter, diameter, dieSizeY/2)
X, Y = np.meshgrid(x, y)

extent = np.min(x), np.max(x), np.min(y), np.max(y)
fig = plt.figure(frameon=False)

Z = np.array(([0,0.5],[0.3,0.1])) 
im1 = plt.imshow(Z, cmap=plt.cm.viridis, interpolation='nearest',
                  extent=extent)



plt.show()"""