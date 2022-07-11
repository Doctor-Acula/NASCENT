# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:26:14 2022

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
    def __init__(center, x, y):
        center.x = x
        center.y = y
        
#Printing coordinates of center points of dice using for loops# 
print("Center coordinates for all Dice: \n")         
for i in range(0,len(dieCenterX)):
    for j in range(0,len(dieCenterY)):
        d1 = Dice(dieCenterX[i], dieCenterY[j])
        print(d1.x)
        print(d1.y)
        print("\n")
        
        
        
###### Defining Vertices ######    

#Creating arrays for the x and y coordinates of die VERTEX 1#    
v1X = (np.arange((dieSizeX-(diameter/2)), ((diameter/2)+0.1), (dieSizeX))) 
v1Y = v1X
    
#Creating a class to define the coordinates of vertex 1#
class Vertex1:
    def __init__(V1, x, y):
        V1.x = x
        V1.y = y
        
#Printing coordinates of vertex1 of dice using for loops# 
print("V1 Coordinates for all Dice: \n")         
for i in range(0,len(v1X)):
    for j in range(0,len(v1Y)):
        V1 = Vertex1(v1X[i], v1Y[j])
        print(V1.x)
        print(V1.y)
        print("\n")

#Creating arrays for the x and y coordinates of die VERTEX 2#    
v2X = -v1X #This is essentially just a mirror of the x-coordinates of vertex 1 
v2Y = v1Y
    
#Creating a class to define the coordinates of vertex 1#
class Vertex2:
    def __init__(V2, x, y):
        V2.x = x
        V2.y = y
        
#Printing coordinates of vertex1 of dice using for loops# 
print("V2 Coordinates for all Dice: \n")         
for i in range(0,len(v2X)):
    for j in range(0,len(v2Y)):
        V2 = Vertex2(v2X[i], v2Y[j])
        print(V2.x)
        print(V2.y)
        print("\n")
        
#Creating arrays for the x and y coordinates of die VERTEX 3#    
v3X = -v1X  
v3Y = -v1Y #This is essentially just a mirror of the x and y coordinates of vertex 1
    
#Creating a class to define the coordinates of vertex 3#
class Vertex3:
    def __init__(V3, x, y):
        V3.x = x
        V3.y = y
        
#Printing coordinates of vertex3 of dice using for loops# 
print("V3 Coordinates for all Dice: \n")         
for i in range(0,len(v3X)):
    for j in range(0,len(v3Y)):
        V3 = Vertex3(v3X[i], v3Y[j])
        print(V3.x)
        print(V3.y)
        print("\n")
        
#Creating arrays for the x and y coordinates of die VERTEX 4#    
v4X = v1X  
v4Y = -v1Y 
    
#Creating a class to define the coordinates of vertex 3#
class Vertex4:
    def __init__(V4, x, y):
        V4.x = x
        V4.y = y
        
#Printing coordinates of vertex3 of dice using for loops# 
print("V4 Coordinates for all Dice: \n")         
for i in range(0,len(v4X)):
    for j in range(0,len(v4Y)):
        V4 = Vertex4(v4X[i], v4Y[j])
        print(V4.x)
        print(V4.y)
        print("\n")
        
###### Creating a list of all dice within the wafer circle ######
WholeDice = []
print(WholeDice)
test = [1,2,3,4,5,6]
WholeDice.append(test)
print(WholeDice)



###### Generating the Plot ######
x = np.arange(-diameter, diameter, dieSizeX/2)
y = np.arange(-diameter, diameter, dieSizeY/2)
X, Y = np.meshgrid(x, y)

extent = np.min(x), np.max(x), np.min(y), np.max(y)
fig = plt.figure(frameon=False)

Z = np.array(([0,0.5],[0.3,0.1])) 
im1 = plt.imshow(Z, cmap=plt.cm.viridis, interpolation='nearest',
                  extent=extent)



plt.show()