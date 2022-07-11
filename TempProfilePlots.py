# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:17:40 2022

@author: et24233
"""

#Plotting spatial profile
import matplotlib.pyplot as plt
  
x = [0,0,1.5,1.5,3,3,4,4]
y = [0,2,2,1,1,1.5,1.5,0]
plt.plot(x, y)
  
plt.xlabel('Width (nm)')
plt.ylabel('Height (nm)')
plt.title('Spatial Profile')
  
plt.show()

#Establishing temperature profile via spatial profile (this removes
#the starting and ending y values of 0)
y_ = y[1:-1]
    

#Choosing a base temperature at which the etching process will run
###base_temp = input("At what maximum temperature should the process run? (celsius)")
###base_temp = int(base_temp) #Inputs are not working right now. Fix this later!

base_temp = 400

thickest = max(y_)
unit_vals = [i * (1/thickest) for i in y_]
tempy = [i * base_temp for i in unit_vals]

tempx = x[1:-1]

plt.plot(tempx, tempy)
  
plt.xlabel('Width (nm)')
plt.ylabel('Temp (c)')
plt.title('Temperature Profile')
  
plt.show()

  