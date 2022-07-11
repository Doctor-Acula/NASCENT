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
for i in range(0,len(dieCenterX)):
    for j in range(0,len(dieCenterY)):
        dieCenter = np.array(([dieCenterX[i], dieCenterY[j]]))
        
        v1X = dieCenterX[i]+(dieSizeX/2)
        v1Y = dieCenterY[j]+(dieSizeY/2)
        v1 = np.array(([v1X, v1Y]))
        
        v2X = dieCenterX[i]-(dieSizeX/2)
        v2Y = dieCenterY[j]+(dieSizeY/2)
        v2 = np.array(([v2X, v2Y]))
        
        v3X = dieCenterX[i]-(dieSizeX/2)
        v3Y = dieCenterY[j]-(dieSizeY/2)
        v3 = np.array(([v3X, v3Y]))
        
        v4X = dieCenterX[i]+(dieSizeX/2)
        v4Y = dieCenterY[j]-(dieSizeY/2)
        v4 = np.array(([v4X, v4Y]))
        
        print("Die Center:")
        print(dieCenter)
        print("V1: ")
        print(v1)
        print("v2:")
        print(v2)
        print("v3:")
        print(v3)
        print("V4:")
        print(v4)
        
        
        print("\n")
        
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