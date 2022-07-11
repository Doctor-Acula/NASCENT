# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 13:04:47 2022

@author: et24233
"""
import math
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

############################################
#Manually input LED radiant flux in W  and LED grid size here:#
QLed = 1.1

GridM = 30 #The LED grids can have an M # N area
GridN = 30 

Qi = QLed*(GridM*GridN)
####################
#Wafer measurements#

r = 0.15 # Radius of wafer in m 
h = 7.75*(10**-4) # Wafer thickness 
v = math.pi*(r**2)*h #Volume of substrate given radius and thickness

#######################################
#Stefan-Boltzmann variable declaration#

e = 0.7 #emissivity for silicon
o = 5.6703*(10**-8) #Stefan-Boltzmann Constant
A = math.pi*(r**2) #Area of entire wafer 

#############################
#Q=mcAT Variable Declaration#

m = ((2.329*(10**6))*v)/1000 #mass in kilograms
c = 710 #specific heat capacity of silicon in J/kg*K 

################################
#Defining differential equation#

def T(t, T):
    Qo = 2*A*e*o*(T**4) #Stefan-Boltzmann Equation (placed in this function so T varies and isn't declared to be 273.15). The "2" comes from the fact their are two surfaces on the substrate (top and bottom)
    dTdt = (((Qi)-(Qo))/(m*c))
    return dTdt

################################################################
#Solving the initial value problem using the Runge-Kutta method#

sol = solve_ivp(T, [0, 125], [293.15]) #([Function name], [Limits of integration], [Initial value (y0)]) 

#########################   
#Plotting the solved IVP#

plt.figure()
fig, ax = plt.subplots(num=1)
ax.plot(sol.t, sol.y[0]-273.15, 'k-') #The "sol.y[0]-273.15" here converts Kelvin to Celsius. Remove the "-273.15" portion to keep temperature in Kelvin (don't forget to update y-axis label)

######################
#Defining Plot labels#

plt.title("Temperature of Silicon Wafer with %.3f W LEDs " %QLed + "in a %i x " %GridM + "%i Grid" %GridN)
plt.ylabel("Temperature (c)")
plt.xlabel("Time (s)")
plt.show()

#####################
#General Information#

fluxDensity = Qi/A
print('Flux Density in W/cm2 is', fluxDensity/(100*100))

#####################
