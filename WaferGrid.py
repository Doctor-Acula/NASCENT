# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:08:25 2022

@author: et24233
"""

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

#Wafer Parameters#
diameter = 100
dieSizeX = 10
dieSizeY = 10
dieMaxThickness = 700 # Die max thickness in Microns 
ttvPitch = 0.25

rSquared = (diameter/2)**2 
d1 = []


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

#Creating a class to define center points and vertices#
class Dice:
    def __init__(self, center, V1,V2,V3,V4, thickness):
        self.center = center
        self.V1 = V1
        self.V2 = V2
        self.V3 = V3
        self.V4 = V4
        self.thickness = thickness
        
#Defining coordinates of center points and vertices of dice using "for" loop#  
thicknessList = []        
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
        
        v1Squared = np.square(v1)
        v2Squared = np.square(v2)
        v3Squared = np.square(v3)
        v4Squared = np.square(v4)
        SumV1Squared = sum(v1Squared)
        SumV2Squared = sum(v2Squared)
        SumV3Squared = sum(v3Squared)
        SumV4Squared = sum(v4Squared)
        
        if SumV1Squared <= rSquared and SumV2Squared <= rSquared and SumV3Squared <= rSquared and SumV4Squared <= rSquared :
             thickness = dieMaxThickness*(0.5 + 0.25*(np.sin(2*np.pi*(dieCenterX[i])/ttvPitch)) + 0.25*(np.sin(2*np.pi*(dieCenterY[j])/ttvPitch)))
             d1.append(Dice(dieCenter, v1, v2, v3, v4,thickness))
             #print('thickness', thickness)
             thicknessList.append(thickness) 
        
        #print("\n")    
       
###### Generating the Plot ######

k = 0
dieThicknessPlot = np.zeros(([len(dieCenterX),len(dieCenterY)]))
for i in range(0,len(dieCenterX)):
    for j in range (0,len(dieCenterY)): 
        if (np.sqrt((dieCenterX[i]+dieSizeX/2)**2 + (dieCenterY[j]+dieSizeY/2)**2) < (diameter/2) and 
            np.sqrt((dieCenterX[i]-dieSizeX/2)**2 + (dieCenterY[j]+dieSizeY/2)**2) < (diameter/2) and 
            np.sqrt((dieCenterX[i]+dieSizeX/2)**2 + (dieCenterY[j]-dieSizeY/2)**2) < (diameter/2) and
            np.sqrt((dieCenterX[i]-dieSizeX/2)**2 + (dieCenterY[j]-dieSizeY/2)**2) < (diameter/2)):
                dieThicknessPlot[i][j] = d1[k].thickness - min(thicknessList) #
                k += 1 

extent = np.min(dieCenterX)-dieSizeX/2, np.max(dieCenterX)+dieSizeX/2, np.min(dieCenterY)-dieSizeY/2, np.max(dieCenterY)+dieSizeY/2
im = plt.imshow(dieThicknessPlot, cmap=plt.cm.viridis, interpolation='nearest',extent=extent)

ax = plt.subplot()
plt.title("Thicknesses of WHOLE Wafer Dice (m)")
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.45)

plt.colorbar(im, cax=cax)

plt.show()


########################################
##### LED Parameters ######
LEDx = 4.4
LEDy = 4.4
power = 1.1
area = dieSizeX*dieSizeY

###### Defining LED Center Points ######  
LEDCenterPosX = (np.arange((dieSizeX/2), (diameter/2), (dieSizeX))) 
LEDCenterNegX = dieCenterPosX*-1 
LEDCenterX = np.concatenate((dieCenterNegX, dieCenterPosX), axis=0)
LEDCenterX.sort()

LEDCenterPosY =  (np.arange((dieSizeY/2), (diameter/2), (dieSizeY)))
LEDCenterNegY = dieCenterPosY*-1
LEDCenterY = np.concatenate((dieCenterNegY, dieCenterPosY), axis=0)
LEDCenterY.sort()

#Creating a class to define a grid of LEDs#
class LEDs:
    def __init__(self, center, V1,V2,V3,V4, intensity):
        self.center = center
        self.V1 = V1
        self.V2 = V2
        self.V3 = V3
        self.V4 = V4
        self.intensity = intensity

#Printing coordinates of center points and vertices of LEDs using "for" loops#         
for i in range(0,len(dieCenterX)):
    for j in range(0,len(dieCenterY)):
        LEDCenter = np.array(([LEDCenterX[i], LEDCenterY[j]]))
        
        Lv1X = LEDCenterX[i]+(LEDx/2)
        Lv1Y = LEDCenterY[j]+(LEDy/2)
        Lv1 = np.array(([Lv1X, Lv1Y]))
        
        Lv2X = LEDCenterX[i]-(LEDx/2)
        Lv2Y = LEDCenterY[j]+(LEDy/2)
        Lv2 = np.array(([Lv2X, Lv2Y]))
        
        Lv3X = LEDCenterX[i]-(LEDx/2)
        Lv3Y = LEDCenterY[j]-(LEDy/2)
        Lv3 = np.array(([Lv3X, Lv3Y]))
        
        Lv4X = LEDCenterX[i]+(LEDx/2)
        Lv4Y = LEDCenterY[j]-(LEDy/2)
        Lv4 = np.array(([Lv4X, Lv4Y]))
        
        intensity = power/area
        
        print("LED Center:", LEDCenter)
        print("V1:", Lv1)
        print("V2:", Lv2)
        print("V3:", Lv3)
        print("V4:", Lv4)
        print("LED Intensity:", round(intensity, 3)) #Watts/m^2
        print("\n")
        
        Lv1Squared = np.square(Lv1)
        Lv2Squared = np.square(Lv2)
        Lv3Squared = np.square(Lv3)
        Lv4Squared = np.square(Lv4)
        SumLV1Squared = sum(Lv1Squared)
        SumLV2Squared = sum(Lv2Squared)
        SumLV3Squared = sum(Lv3Squared)
        SumLV4Squared = sum(Lv4Squared)
        
        if SumLV1Squared <= rSquared and SumLV2Squared <= rSquared and SumLV3Squared <= rSquared and SumLV4Squared <= rSquared :
             print("This LED is in the wafer boundary")
 
        
        print("\n")    