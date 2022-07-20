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
dieSizeX = 20
dieSizeY = 20
dieMaxThickness = 700 # Die max thickness in Microns 
ttvPitch = 0.25

rSquared = (diameter/2)**2 
dieList = []


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
             dieList.append(Dice(dieCenter, v1, v2, v3, v4,thickness))
             thicknessList.append(thickness)     
       
###### Generating the Plot ######
k = 0
dieThicknessPlot = np.zeros(([len(dieCenterX),len(dieCenterY)]))
for i in range(0,len(dieCenterX)):
    for j in range (0,len(dieCenterY)): 
        if (np.sqrt((dieCenterX[i]+dieSizeX/2)**2 + (dieCenterY[j]+dieSizeY/2)**2) < (diameter/2) and 
            np.sqrt((dieCenterX[i]-dieSizeX/2)**2 + (dieCenterY[j]+dieSizeY/2)**2) < (diameter/2) and 
            np.sqrt((dieCenterX[i]+dieSizeX/2)**2 + (dieCenterY[j]-dieSizeY/2)**2) < (diameter/2) and
            np.sqrt((dieCenterX[i]-dieSizeX/2)**2 + (dieCenterY[j]-dieSizeY/2)**2) < (diameter/2)):
                dieThicknessPlot[i][j] = dieList[k].thickness - min(thicknessList) #
                k += 1 

extent = np.min(dieCenterX)-dieSizeX/2, np.max(dieCenterX)+dieSizeX/2, np.min(dieCenterY)-dieSizeY/2, np.max(dieCenterY)+dieSizeY/2
im = plt.imshow(dieThicknessPlot, cmap=plt.cm.viridis, interpolation='nearest',extent=extent)

ax = plt.subplot()
plt.title("Thicknesses of WHOLE Wafer Dice")
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.45)

plt.colorbar(im, cax=cax)
plt.title("   (m)", loc= 'left')

plt.show()


############################
##### LED Parameters ######
LEDx = 4.4 #Dimensions of LEDs themselves
LEDy = 4.4
LEDGridX = 100 #Dimensions of LED grid
LEDGridY = 100
power = 1.1
pitch = 20
LEDList = []

#Creating a class to define a grid of LEDs#
class LEDs:
    def __init__(self, center, V1,V2,V3,V4, intensity, kV1, kV2, kV3, kV4):
        self.center = center
        self.V1 = V1
        self.V2 = V2
        self.V3 = V3
        self.V4 = V4
        self.intensity = intensity
        self.kV1 = kV1
        self.kV2 = kV2
        self.kV3 = kV3
        self.kV4 = kV4

#Printing coordinates of center points and vertices of LEDs using "for" loops#  
intensity = power/(LEDx*LEDy)

LEDCenterPosX = np.arange(pitch/2, diameter/2, pitch) 
LEDCenterNegX = LEDCenterPosX*-1 
LEDCenterX = np.concatenate((LEDCenterNegX, LEDCenterPosX), axis=0)
LEDCenterX.sort()

LEDCenterPosY =  np.arange(pitch/2, diameter/2, pitch)
LEDCenterNegY = LEDCenterPosY*-1
LEDCenterY = np.concatenate((LEDCenterNegY, LEDCenterPosY), axis=0)
LEDCenterY.sort() 

### Kernel Parameters ###
klengthX = (2*np.max(dieCenterX)+dieSizeX)/len(LEDCenterX) 
klengthY = (2*np.max(dieCenterY)+dieSizeY)/len(LEDCenterY) 

       
for i in range(0, (int(LEDGridX/pitch)-1)): 
    for j in range(0, (int(LEDGridX/pitch)-1)):
        
        
        LEDCenter = np.array(([LEDCenterX[i], LEDCenterY[j]]))
        
        ########################
        
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
        
        
        Lv1Squared = np.square(Lv1)
        Lv2Squared = np.square(Lv2)
        Lv3Squared = np.square(Lv3)
        Lv4Squared = np.square(Lv4)
        SumLV1Squared = sum(Lv1Squared)
        SumLV2Squared = sum(Lv2Squared)
        SumLV3Squared = sum(Lv3Squared)
        SumLV4Squared = sum(Lv4Squared)
        
        Kv1X = LEDCenterX[i]+(klengthX/2)
        Kv1Y = LEDCenterY[j]+(klengthY/2)
        Kv1 = np.array(([Kv1X, Kv1Y]))
        
        Kv2X = LEDCenterX[i]-(klengthX/2)
        Kv2Y = LEDCenterY[j]+(klengthY/2)
        Kv2 = np.array(([Kv2X, Kv2Y]))
        
        Kv3X = LEDCenterX[i]-(klengthX/2)
        Kv3Y = LEDCenterY[j]-(klengthY/2)
        Kv3 = np.array(([Kv3X, Kv3Y]))
        
        Kv4X = LEDCenterX[i]+(klengthX/2)
        Kv4Y = LEDCenterY[j]-(klengthY/2)
        Kv4 = np.array(([Kv4X, Kv4Y]))    
        
        print("Kernel Center:", LEDCenter)
        print("V1:", Kv1)
        print("V2:", Kv2)
        print("V3:", Kv3)
        print("V4:", Kv4)
        print("\n")
    
        
        if SumLV1Squared <= rSquared and SumLV2Squared <= rSquared and SumLV3Squared <= rSquared and SumLV4Squared <= rSquared :
             LEDList.append(LEDs(LEDCenter, Lv1, Lv2, Lv3, Lv4, intensity, Kv1, Kv2, Kv3, Kv4))

### Determining if dice areas and kernel areas overlap ###

pDiceLED = np.zeros((len(dieList), len(LEDList))) #a zero matrix of size number of dice * number of LED's 
for i in range(0, len(dieList)): #for i in range (0, length of die list):
    for j in range(0, len(LEDList)): #for j in range (0, length of led list):
        R1 = [dieList[i].V3[0], dieList[i].V3[1], dieList[i].V1[0], dieList[i].V1[1]]
        R2 = [LEDList[j].kV3[0], LEDList[j].kV3[1], LEDList[j].kV1[0], LEDList[j].kV1[1]]
        
        if (R1[0]>=R2[2]) or (R1[2]<=R2[0]) or (R1[3]<=R2[1]) or (R1[1]>=R2[3]):
            pDiceLED[i][j] = 0
        else:
            av1x = np.min((dieList[i].V1[0],LEDList[j].kV1[0]))
            av1y = np.min((dieList[i].V1[1],LEDList[j].kV1[1]))
            av3x = np.min((dieList[i].V3[0],LEDList[j].kV3[0]))
            av3y = np.min((dieList[i].V3[1],LEDList[j].kV3[1]))
                
            overlapArea = (abs(av1y-av3y))*(abs(av1x-av3x))
            
            print('Die id in overlap: ',i)
            print('die center: ',dieList[i].center)
            print('Die V1: ', dieList[i].V1)
            print('Die V3:', dieList[i].V3)
            print('LED id in overlap: ',j)
            print('LED Center: ', LEDList[j].center)
            print('LED-V1:',LEDList[j].kV1)
            print('LED-V3:',LEDList[j].kV3)
            print()
        
            pDiceLED[i,j] = (overlapArea/(klengthX*klengthY))  #The overlap area between the ith die and jth LED 
  